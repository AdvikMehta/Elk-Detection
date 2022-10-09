"""
    Program to shuffle files in a folder and rename them from 1 to n
    Assumes the number of images are less than 9999 for renaming
    Saves in jpg format
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