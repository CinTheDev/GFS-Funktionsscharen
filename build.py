import os
import shutil
import subprocess

def get_scene_filenames(scenes):
    filenames = []

    for scene in scenes:
        filenames.append(scene + '.py')
    
    return filenames

scenes = [
    "opening",
    "placeholder",
]
scene_files = get_scene_filenames(scenes)

# Create empty "out" directory
if os.path.isdir('out'):
    shutil.rmtree('out')

os.mkdir('out')
os.mkdir('out/vid')

# Compile and copy presenter program
subprocess.run(['cargo', 'build', '--release'], cwd='mp4-presenter')
shutil.copy2('mp4-presenter/target/release/mp4-presenter', 'out/mp4-presenter')

# Render and copy animations
subprocess.run(['./render.sh'] + scene_files, cwd='animation')
