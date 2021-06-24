#!/bin/bash -xe

PROJECT_DIR="$(dirname "$0")/.."
SOURCE_APP="src"
cd "$PROJECT_DIR"

#
# SOURCE CODE
#
rm -rf dist \
  && mkdir -p dist \
  && zip -r "$SOURCE_APP.zip" "$SOURCE_APP" \
  && mv "$SOURCE_APP.zip" dist/ \
  && cp main.py dist/

#
# SCRIPTS
#
mkdir -p dist/scripts \
  && cp scripts/pipe-* dist/scripts/

#
# PERMISSIONS
# How this "dist" will be generated inside a docker container
# we have to make sure that you are going to be able to use and edit it.
#
chmod -R 777 dist/

exit 0
