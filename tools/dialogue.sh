#!/bin/sh

if [ $# -ne 1 ]; then
  echo "using: $0 [mas version]" 1>&2
  exit 1
fi

MAS_VERSION=$1

echo "Fix ZeroDivisionError"
# / float(mas_getTotalSessions())
sed -i 's/float(mas_getTotalSessions())/float(1)/g' "/tmp/mas-$MAS_VERSION/game/updates.rpy"

echo "Add mark translatable strings"
# prompt="Thoughts on God"
sed -i -r 's/prompt="([^"]+)"/prompt=_\("\1"\)/g' "/tmp/mas-$MAS_VERSION/game/**.rpy"
# $ renpy.say(m, "What kind of weather would you like?", interact=False)
sed -i -r 's/(renpy.say\(\w+, )"([^"]+)"/\1_\("\2"\)/g' "/tmp/mas-$MAS_VERSION/game/**.rpy"

echo "Extract dialogs Monika After Story $MAS_VERSION"
/tmp/renpy/renpy.sh "/tmp/mas-$MAS_VERSION" dialogue --strings --escape
sed "s|$(pwd)|game|" "/tmp/mas-$MAS_VERSION/dialogue.tab" >./dialogue.tab
