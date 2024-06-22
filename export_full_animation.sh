#!/bin/bash

python3 build.py

(
    cd out/vid
    find *.mp4 | sed 's:\ :\\\ :g' | sed 's/^/file /' > file-list.txt
    ffmpeg -f concat -i file-list.txt -c copy output.mp4
    mv output.mp4 ../full-animation.mp4
    rm file-list.txt
)
