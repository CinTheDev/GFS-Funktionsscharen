import sys
import os
import shutil
import subprocess

def get_start_scene():
    try:
        input_string = sys.argv[1]
        start_scene = int(input_string)
        return start_scene
    except:
        return 0

scenes = [
    "opening",
    "intro_graph_parameter",
    "intro_graph_properties",
    "calculation_insertion",
    "calculation_nullstellen",
    "calculation_turning_points",
    "calculation_verification_graph",

    "analysis_exponential",
    "visualize_analysis_exponential",
    "analysis_exponential_2",
    "visualize_analysis_exponential_2",

    "practice_1",
    "practice_2_analysis",
]

# Create empty "out" directory
if os.path.isdir('out'):
    shutil.rmtree('out')

os.mkdir('out')
os.mkdir('out/vid')

# Compile and copy presenter program
subprocess.run(['cargo', 'build', '--release'], cwd='mp4-presenter')
shutil.copy2('mp4-presenter/target/release/mp4-presenter', 'out/mp4-presenter')

# Render and copy animations
subprocess.run(['python3', 'render.py'] + scenes, cwd='animation')

start_index = get_start_scene()

for i in range(start_index, len(scenes)):
    sections = 'animation/media/videos/' + scenes[i] + '/1080p60/sections'

    for entry in os.scandir(sections):
        if not entry.is_file() or not entry.name.endswith('.mp4'):
            continue

        new_filename = "{index:03d}_{name}".format(index=i, name=entry.name)
        shutil.copy2(entry.path, 'out/vid/' + new_filename)
