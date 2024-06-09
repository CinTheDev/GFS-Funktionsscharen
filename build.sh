#!/bin/bash

# This script will render the animations and compile the presentation program
# and put it together into a directory

SCENES=(
    "opening.py"
    "placeholder.py"
)
SCENE_AMOUNT="${#SCENES[@]}"

if [[ -d out ]]; then
    rm -rf out
fi

mkdir out
mkdir out/vid

# Presenter
(
    cd mp4-presenter
    cargo build --release
)
cp mp4-presenter/target/release/mp4-presenter out/mp4-presenter

# Animations
(
    cd animation
    ./render.sh "${SCENES[@]}"
)
cp -r animation/media/videos/opening/1080p60/sections/*.mp4 out/vid/
