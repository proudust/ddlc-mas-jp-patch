if [ $# -ne 1 ]; then
  echo "using: $0 [mas version]" 1>&2
  exit 1
fi

MAS_VERSION=$1

result=0
`dirname $0`/dependencies.sh $MAS_VERSION || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

echo "Extract dialogs Monika After Story $MAS_VERSION"
/tmp/renpy/renpy.sh /tmp/mas-$MAS_VERSION dialogue --strings --escape
sed "s|`pwd`|game|" /tmp/mas-$MAS_VERSION/dialogue.tab >./dialogue.tab
