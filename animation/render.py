import sys
import os
import shutil
import subprocess

checksum_dir = 'media/checksums'
checksum_file = checksum_dir + '/animation-checksums.txt'
checksum_file_old = checksum_dir + '/animation-checksums.old.txt'

checksums = []

if os.path.isfile(checksum_file):
    f = open(checksum_file, "r")

    for line in f:
        checksums.append(line)
    
    f.close()
    os.rename(checksum_file, checksum_file_old)

scenes = sys.argv[1:]

for i in range(len(scenes)):
    scene_filename = scenes[i] + '.py'
    if i < len(checksums):
        checksum = subprocess.check_output(['md5sum', scene_filename]).decode('utf-8')

        # Skip rendering if checksum matches
        if checksum == checksums[i]:
            print(scene_filename + " already rendered. Skipping...")
            continue

    # Remove sections
    sections_path = 'media/videos/' + scenes[i] + '/1080p60/sections/'
    if os.path.isdir(sections_path):
        shutil.rmtree(sections_path)

    # Render the scene
    subprocess.run(['manim', 'render', '-qh', '-a', '--save_sections', scene_filename])

if not os.path.isdir(checksum_dir):
    os.mkdir(checksum_dir)

f = open(checksum_file, "w")

for scene in scenes:
    scene_filename = scene + '.py'
    checksum = subprocess.check_output(['md5sum', scene_filename]).decode('utf-8')
    f.write(checksum)

f.close()
