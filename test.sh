#!/bin/bash

python3 build.py $1

(
    cd out
    ./mp4-presenter
)
