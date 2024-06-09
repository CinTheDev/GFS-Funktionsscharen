#!/bin/bash

CHECKSUM_DIR="/tmp/gfs-funktionsscharen"
CHECKSUM_FILE="$CHECKSUM_DIR/animation-checksums.txt"

# Render all specified scenes
for scene in "$@"
do
    manim render -qh -a --save_sections "$scene"
done

if [[ -d $CHECKSUM_DIR ]]; then
    rm -rf $CHECKSUM_DIR
fi

mkdir -p $CHECKSUM_DIR

for scene in "$@"
do
    checksum=$(md5sum "$scene")
    echo $checksum >> $CHECKSUM_FILE
done
