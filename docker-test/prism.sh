#!/bin/bash

set -eu

install () {

echo "Installing Prism..."

UNAME=$(uname)
ARCH=$(uname -m)
if [ "$UNAME" != "Linux" ] && [ "$UNAME" != "Darwin" ] && [ "$ARCH" != "x86_64" ] && [ "$ARCH" != "i686" ]; then
    echo "Sorry, OS/Architecture not supported: ${UNAME}/${ARCH}. Download binary from https://github.com/stoplightio/prism/releases"
    exit 1
fi

if [ "$UNAME" = "Darwin" ] ; then
  OSX_ARCH=$(uname -m)
  if [ "${OSX_ARCH}" = "x86_64" ] ; then
    PLATFORM="darwin_amd64"
  fi
elif [ "$UNAME" = "Linux" ] ; then
  LINUX_ARCH=$(uname -m)
  if [ "${LINUX_ARCH}" = "i686" ] ; then
    PLATFORM="linux_386"
  elif [ "${LINUX_ARCH}" = "x86_64" ] ; then
    PLATFORM="linux_amd64"
  fi
fi

mkdir -p ../prism/bin
#LATEST=$(curl -s https://api.github.com/repos/stoplightio/prism/tags | grep -Eo '"name":.*?[^\\]",'  | head -n 1 | sed 's/[," ]//g' | cut -d ':' -f 2)
LATEST="v0.6.21"
URL="https://github.com/stoplightio/prism/releases/download/$LATEST/prism_$PLATFORM"
DEST=../prism/bin/prism

if [ -z $LATEST ] ; then
  echo "Error requesting. Download binary from ${URL}"
  exit 1
else
  curl -L $URL -o $DEST
  chmod +x $DEST
fi
}

if [ -f ../prism/bin/prism ]; then
   echo "Prism is already installed."
else
   echo "Prism is not installed."
   install
fi