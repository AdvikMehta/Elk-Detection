"""
    Program to shuffle files in a folder and rename them from 1 to n
    Assumes the number of images are less than 9999 for renaming
    Saves in jpg format

    img_dir = {img1.jpg, img2.jpg, img3.jpg, img4.jpg, img5.jpg}
    ==================================================================
    img_dir = {1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg} *
"""

from os import listdir, rename
from os.path import isfile, join
from random import shuffle

# path = 'elk-images/'
path = 'MYPATH'
files = [f for f in listdir(path) if isfile(join(path, f))]
shuffle(files)
# num_zeroes = int(math.log10(len(files))) + 1

num = 1
for old_name in files:
    new_name = "%04d" % (num,) + ".jpg"
    rename(path + old_name, path + new_name)
    num += 1