import sys
import os
import shutil
import subprocess

checksum_dir = '/tmp/gfs-funktionsscharen'
checksum_file = checksum_dir + '/animation-checksums.txt'

for scene in sys.argv[1:]:
    subprocess.run(['manim', 'render', '-qh', '-a', '--save-sections', scene])

if os.path.isdir(checksum_dir):
    shutil.rmtree(checksum_dir)

os.mkdir(checksum_dir)

for scene in sys.argv[1:]:
    checksum = ""
    subprocess.run(['md5sum', scene], stdout=checksum)
    print(checksum)
