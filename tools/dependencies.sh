#!/bin/sh

if [ $# -ne 1 ]; then
    echo "using: $0 [mas version]" 1>&2
    exit 1
fi

MAS_VERSION=$1

if [ ! -f sdk/renpy.sh ]; then
    echo "Download Ren'Py SDK v6.99.12.4"
    wget -q -O renpy.tar.bz2 https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
    tar -xf renpy.tar.bz2
    rm renpy.tar.bz2
    mv renpy-6.99.12.4-sdk sdk

    echo "Apply Extract Dialogue patch to Ren'Py"
    wget -q -O sdk/renpy/translation/dialogue.py https://raw.githubusercontent.com/proudust/renpy/dialogue-patch/renpy/translation/dialogue.py
fi

if [ ! -d "/tmp/mas-$MAS_VERSION" ]; then
    if [ ! -d /tmp/ddlc ]; then
        echo "Download Doki Doki Literature Club! v1.1.1"
        wget -qO /tmp/ddlc.zip "$(curl -qsX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url)"
        unzip -q /tmp/ddlc.zip -d /tmp
        rm /tmp/ddlc.zip
        mv /tmp/DDLC-1.1.1-pc/ /tmp/ddlc/
    fi

    if [ ! -f unrpyc/unrpyc.py ]; then
        echo "Download unrpyc"
        git clone https://github.com/CensoredUsername/unrpyc.git unrpyc >/dev/null
    fi

    echo "Download Monika After Story $MAS_VERSION"
    ASSET_ID=$(curl -sL "https://api.github.com/repos/Monika-After-Story/MonikaModDev/releases/tags/$MAS_VERSION" | jq '.assets[] | select(.name | test("Monika_After_Story-\\d+.\\d+.\\d+-Mod.zip")) | .id')
    if [ "$ASSET_ID" = 'null' ]; then
        echo "ERROR: version $MAS_VERSION does not exist"
        exit 1
    fi
    wget -qO "/tmp/mas-$MAS_VERSION.zip" --header='Accept: application/octet-stream' "https://api.github.com/repos/Monika-After-Story/MonikaModDev/releases/assets/$ASSET_ID"
    cp -fpr /tmp/ddlc/ "/tmp/mas-$MAS_VERSION/"
    rm -f "/tmp/mas-$MAS_VERSION/game/*.rpy" "/tmp/mas-$MAS_VERSION/game/*.rpyc"
    if unzip -l "/tmp/mas-$MAS_VERSION.zip" | grep -q game/; then
        unzip -oq "/tmp/mas-$MAS_VERSION.zip" -d "/tmp/mas-$MAS_VERSION/"
    else
        unzip -oq "/tmp/mas-$MAS_VERSION.zip" -d "/tmp/mas-$MAS_VERSION/game/"
    fi
    rm "/tmp/mas-$MAS_VERSION.zip"

    echo "Decompile Monika After Story $MAS_VERSION"
    python2 unrpyc/unrpyc.py "/tmp/mas-$MAS_VERSION/game/*.rpyc"
fi
