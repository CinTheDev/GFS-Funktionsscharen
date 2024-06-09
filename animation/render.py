import sys
import os
import shutil
import subprocess

checksum_dir = '/tmp/gfs-funktionsscharen'
checksum_file = checksum_dir + '/animation-checksums.txt'

checksums = []

if os.path.isfile(checksum_file):
    f = open(checksum_file, "r")

    for line in f:
        checksums.append(line)
    
    f.close()
    shutil.rmtree(checksum_dir)

scenes = sys.argv[1:]

for i in range(len(scenes)):
    if i < len(checksums):
        checksum = subprocess.check_output(['md5sum', scenes[i]]).decode('utf-8')

        # Skip rendering if checksum matches
        if checksum == checksums[i]:
            print(scenes[i] + " already rendered. Skipping...")
            continue

    subprocess.run(['manim', 'render', '-qh', '-a', '--save_sections', scenes[i]])

os.mkdir(checksum_dir)

f = open(checksum_file, "w")

for scene in scenes:
    checksum = subprocess.check_output(['md5sum', scene]).decode('utf-8')
    f.write(checksum)

f.close()
