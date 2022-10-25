"""
    Program to shuffle images and labels in respective folders and rename them from 1 to n
    Assumes the number of images/labels are less than 9999 for renaming
    Saves in jpg/txt format

    img_dir = {img1.jpg, img2.jpg, img3.jpg, img4.jpg, img5.jpg}
    ==================================================================
    img_dir = {1.jpg, 2.jpg, 3.jpg, 4.jpg, 5.jpg} *
"""

from os import listdir, rename
from os.path import isfile, join
from random import shuffle

# path = 'elk-images/'
IMG_PATH = '../cattle/train/images/'
LABEL_PATH = '../cattle/train/labels/'

files = [f for f in listdir(IMG_PATH) if isfile(join(IMG_PATH, f))]
shuffle(files)

num = 2300
for old_img_name in files:
    old_label_name = old_img_name[:-4] + '.txt'
    new_img_name = "%04d" % (num,) + ".jpg"
    new_label_name = "%04d" % (num,) + ".txt"
    rename(IMG_PATH + old_img_name, IMG_PATH + new_img_name)
    rename(LABEL_PATH + old_label_name, LABEL_PATH + new_label_name)
    num += 1

print('Renamed',len(files),'files successfully!')