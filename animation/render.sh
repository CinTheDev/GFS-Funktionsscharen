#!/bin/bash

# Render all specified scenes
for scene in "$@"
do
    manim render -qh -a --save_sections "$scene"
done
