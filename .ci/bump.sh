#!/usr/bin/env sh

# this is not to be run, this is just for testing.
VERSION=''
RELEASE_TYPE="false"
#(git tag --list "0.0.*"  --sort=-version:refname | head -n 1) |python ./.ci/getversion.py $RELEASE_TYPE 2>&1 > $VERSION
#version=$((git tag --list "0.0.*"  --sort=-version:refname | head -n 1) |python ./.ci/getversion.py $RELEASE_TYPE 2>&1)


VERSION=$(git tag --list "0.0.*"  --sort=-version:refname | head -n 1 | python ./.ci/bump_v2.py 2>&1)


echo $VERSION

