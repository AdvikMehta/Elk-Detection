"""
    Program to move images having corresponding labels into a new folder

    img_dir_1 = {img1.jpg, img2.jpg, img3.jpg, img4.jpg, img5.jpg}
    label_dir_1 = {img1.txt, img2.txt, img3.txt}
    img_dir_2 = {}
    ==================================================================
    img_dir_1 = {img1.jpg, img2.jpg, img3.jpg, img4.jpg, img5.jpg}
    label_dir_1 = {img1.txt, img2.txt, img3.txt} *
    img_dir_2 = {img1.jpg, img2.jpg, img3.jpg} *
"""

from os import listdir
from os.path import isfile, join
import shutil

IMGS_PATH = '../model/data/val/all-val-imgs'
LABELS_PATH = '../model/data/val/labels'
NEW_IMG_PATH = '../model/data/val/imgs'

imgs = [f for f in listdir(IMGS_PATH) if isfile(join(IMGS_PATH, f))]
labels = [f for f in listdir(LABELS_PATH) if isfile(join(LABELS_PATH, f))]

imgs_with_labels = []

# removing duplicate labels
labels = list(dict.fromkeys(labels))

# getting images that have corresponding labels
for img in imgs:
    label = imgs[0][:-4] + '.txt'
    if label in labels:
        imgs_with_labels.append(img)

# copying these images to a new folder
for img in imgs_with_labels:
    shutil.copy(join(IMGS_PATH, img), NEW_IMG_PATH)

print('Copied', len(imgs_with_labels), 'images with labels to new destination')