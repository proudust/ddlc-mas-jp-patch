PATCH_VERSION=$(git -C $(dirname $0)/.. describe --tags)
MAS_VERSION=v`grep -oP '(?<=define config.version = ").+(?=")' ./patch/game/options.rpy`

result=0
`dirname $0`/dependencies.sh $MAS_VERSION || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

echo "Inject JP patch version to override.rpy"
sed -i -e "s/\${PATCH_VERSION}/$PATCH_VERSION/" $(dirname $0)/../patch/game/tl/Japanese/overrides.rpy

echo "Build Monika After Story JP patch ver$PATCH_VERSION for $MAS_VERSION"
rm -rf /tmp/mas-jp
cp -fpr /tmp/mas-$MAS_VERSION /tmp/mas-jp
cp -fpr `dirname $0`/../patch/* /tmp/mas-jp

result=0
/tmp/renpy/renpy.sh /tmp/renpy/launcher distribute /tmp/mas-jp --package Mod || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

rm -rf /tmp/mas-jp-dist ./DDLC_MAS_JP_$PATCH_VERSION ./DDLC_MAS_JP_$PATCH_VERSION.zip
unzip -q `ls /tmp/*-dists/*-Mod.zip` -d /tmp/mas-jp-dist
mv `ls -d /tmp/mas-jp-dist/* | head -n1` ./DDLC_MAS_JP_$PATCH_VERSION
zip -q -r ./DDLC_MAS_JP_$PATCH_VERSION.zip ./DDLC_MAS_JP_$PATCH_VERSION
