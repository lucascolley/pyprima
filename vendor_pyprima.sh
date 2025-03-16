#!/bin/bash

# Vendors pyprima from https://github.com/nbelakovski/prima

set -o nounset
set -o errexit

REPO_URL="https://github.com/nbelakovski/prima"
COMMIT_HASH="bb031b16d44bea925dd84ca241b13279d8b121f7"

ROOT_DIR="pyprima"

rm -rf $ROOT_DIR
mkdir $ROOT_DIR
mkdir $ROOT_DIR/.tmp
git clone $REPO_URL $ROOT_DIR/.tmp
pushd $ROOT_DIR/.tmp
git checkout $COMMIT_HASH
popd
mv -v $ROOT_DIR/.tmp/LICENCE.txt $ROOT_DIR/
mv -v $ROOT_DIR/.tmp/pyprima/src/pyprima/__init__.py $ROOT_DIR/
mkdir $ROOT_DIR/common
mv -v $ROOT_DIR/.tmp/pyprima/src/pyprima/common/* $ROOT_DIR/common
mkdir $ROOT_DIR/cobyla
mv -v $ROOT_DIR/.tmp/pyprima/src/pyprima/cobyla/* $ROOT_DIR/cobyla
rm -rf $ROOT_DIR/.tmp

echo "Update this directory using vendor_pyprima.sh" >$ROOT_DIR/README.md
