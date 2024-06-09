import sys
import os
import shutil
import subprocess

checksum_dir = '/tmp/gfs-funktionsscharen'
checksum_file = checksum_dir + '/animation-checksums.txt'

for scene in sys.argv[1:]:
    subprocess.run(['manim', 'render', '-qh', '-a', '--save_sections', scene])

if os.path.isdir(checksum_dir):
    shutil.rmtree(checksum_dir)

os.mkdir(checksum_dir)

f = open(checksum_file, "w")

for scene in sys.argv[1:]:
    checksum = subprocess.check_output(['md5sum', scene])
    f.write(checksum.decode('utf-8'))

f.close()
