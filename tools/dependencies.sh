if [ $# -ne 1 ]; then
  echo "using: $0 [mas version]" 1>&2
  exit 1
fi

MAS_VERSION=$1

if [ ! -f /tmp/renpy/renpy.sh ]; then
  echo "Download Ren'Py SDK v6.99.12.4"
  wget -q -O /tmp/renpy.tar.bz2 https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
  tar -xf /tmp/renpy.tar.bz2 -C /tmp
  rm /tmp/renpy.tar.bz2
  mv /tmp/renpy-6.99.12.4-sdk /tmp/renpy

  echo "Apply Extract Dialogue patch to Ren'Py"
  wget -q -O /tmp/renpy/renpy/translation/dialogue.py https://raw.githubusercontent.com/proudust/renpy/dialogue-patch/renpy/translation/dialogue.py
fi

if [ ! -d /tmp/mas-$MAS_VERSION ]; then
  if [ ! -d /tmp/ddlc ]; then
    echo "Download Doki Doki Literature Club! v1.1.1"
    wget -qO /tmp/ddlc.zip `curl -qsX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url`
    unzip -q /tmp/ddlc.zip -d /tmp
    rm /tmp/ddlc.zip
    mv /tmp/DDLC-1.1.1-pc/ /tmp/ddlc/
  fi

  if [ ! -f /tmp/unrpyc/unrpyc.py ]; then
    echo "Download unrpyc"
    git clone https://github.com/CensoredUsername/unrpyc.git /tmp/unrpyc >/dev/null
  fi

  echo "Download Monika After Story $MAS_VERSION"
  ASSET_ID=`curl -sL https://api.github.com/repos/Monika-After-Story/MonikaModDev/releases/tags/$MAS_VERSION | jq '.assets[0] | .id'`
  if [ "$ASSET_ID" = 'null' ]; then
    echo "ERROR: version $MAS_VERSION does not exist"
    exit 1
  fi
  wget -qO /tmp/mas-$MAS_VERSION.zip --header='Accept: application/octet-stream' https://api.github.com/repos/Monika-After-Story/MonikaModDev/releases/assets/$ASSET_ID
  cp -fpr /tmp/ddlc/ /tmp/mas-$MAS_VERSION/
  unzip -oq /tmp/mas-$MAS_VERSION.zip -d /tmp/mas-$MAS_VERSION/game/
  rm /tmp/mas-$MAS_VERSION.zip

  echo "Decompile Monika After Story $MAS_VERSION"
  python2 /tmp/unrpyc/unrpyc.py /tmp/mas-$MAS_VERSION/game/*.rpyc
fi
