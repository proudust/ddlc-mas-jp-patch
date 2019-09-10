#!/bin/bash
ORIGINAL_GAME_DIR=ddlc

dependents=("wget" "curl" "jq" "unzip")
error=0
for dependent in ${dependents[@]}
do
    if !(type ${dependent} > /dev/null 2>&1); then
        echo "please install ${dependent}!"
        error=1
    fi
done
if [ $error = 1 ]; then
    return 1
fi

cd `dirname ${0}`

if [ ! -d ${ORIGINAL_GAME_DIR} ]; then
    wget -O ddlc.zip `curl -sX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url`
    unzip ddlc.zip
    rm ddlc.zip
    mv DDLC-1.1.1-pc ${ORIGINAL_GAME_DIR}
fi

rm -rf game/
cp -r ${ORIGINAL_GAME_DIR}/game/ ./
cp -r MonikaModDev/Monika\ After\ Story/game/* game/
cp -r patch/game/* game/
