import sys
import os
import shutil
import subprocess

scenes = sys.argv[1:]

for i in range(len(scenes)):
    scene_filename = scenes[i] + '.py'
    scene_dir = "media/videos/" + scenes[i]
    checksum_file = scene_dir + "/checksum.txt"

    if os.path.isfile(checksum_file):
        checksum_io = open(checksum_file, "r")
        saved_checksum = checksum_io.read()
        checksum_io.close()

        current_checksum = subprocess.check_output(['md5sum', scene_filename]).decode('utf-8')

        if saved_checksum == current_checksum:
            print(scene_filename + " already rendered. Skipping...")
            continue

    # Remove sections
    sections_path = 'media/videos/' + scenes[i] + '/1080p60/sections/'
    if os.path.isdir(sections_path):
        shutil.rmtree(sections_path)

    # Render the scene
    subprocess.run(['manim', 'render', '-qh', '-a', '--save_sections', scene_filename])

    # Save checksum of file
    checksum = subprocess.check_output(["md5sum", scene_filename]).decode("utf-8")

    checksum_io = open(checksum_file, "w")
    checksum_io.write(checksum)
    checksum_io.close()
