#!/bin/sh

REPO_ROOT=$(dirname "$0")/..
PATCH_VERSION=$(git -C "$REPO_ROOT" describe --tags)
MAS_VERSION=v$(grep -oP '(?<=renpy.config.version = ").+(?=")' "$REPO_ROOT/game/0config.rpy")

echo "Setup Monika After Story JP patch build"
rm -rf /tmp/mas-jp
cp -fpr "/tmp/mas-$MAS_VERSION" /tmp/mas-jp
cp -fpr "$REPO_ROOT/"* /tmp/mas-jp

echo "Inject JP patch version to override.rpy"
sed -i -e "s/\${PATCH_VERSION}/$PATCH_VERSION/" '/tmp/mas-jp/game/Submods/Japanese Language Submod/jp_main.rpy'

echo "Build Monika After Story JP patch ver$PATCH_VERSION for $MAS_VERSION"
result=0
sdk/renpy.sh sdk/launcher distribute /tmp/mas-jp --package Mod || result=$?
if [ ! "$result" = "0" ]; then
    exit 1
fi

rm -rf /tmp/mas-jp-dist "./DDLC_MAS_JP_$PATCH_VERSION" "./DDLC_MAS_JP_$PATCH_VERSION.zip"
unzip -q "$(find /tmp/*-dists/*-Mod.zip)" -d /tmp/mas-jp-dist
mv "$(find /tmp/mas-jp-dist/* -maxdepth 0)" "./DDLC_MAS_JP_$PATCH_VERSION"
zip -q -r "./DDLC_MAS_JP_$PATCH_VERSION.zip" "./DDLC_MAS_JP_$PATCH_VERSION"
