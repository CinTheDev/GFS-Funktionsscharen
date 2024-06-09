#!/bin/bash

declare -a SCENES=(
    "opening.py"
    "placeholder.py"
)

# Render all scenes
for scene in "${SCENES[@]}"
do
    manim render -qh -a --save_sections "$scene"
done
