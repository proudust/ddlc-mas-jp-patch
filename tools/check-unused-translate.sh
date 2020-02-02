MAS_VERSION=v`grep -oP '(?<=define config.version = ").+(?=")' ./patch/game/options.rpy`

result=0
`dirname $0`/dialogue.sh $MAS_VERSION || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

UNUSED_TRANSLATES=()

while read line
do
  result=0
  grep $line <dialogue.tab >/dev/null 2>&1 || result=$?
  if [ ! "$result" = "0" ]; then
    echo "not found: $line"
    UNUSED_TRANSLATES+=($line)
  fi
done <<END
`grep -hoP '(?<=translate Japanese ).+_[0-9a-f]{8}(?=:)' ./patch/game/tl/Japanese/**.rpy`
END

if [ ${#UNUSED_TRANSLATES[@]} -ne 0 ]; then
  exit 1
fi
