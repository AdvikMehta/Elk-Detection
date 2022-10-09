"""
    Program to move images having corresponding labels into a new folder
"""

from os import listdir
from os.path import isfile, join
import shutil

IMGS_PATH = '../model/data/train/all-train-imgs'
LABELS_PATH = '../model/data/train/labels'
NEW_IMG_PATH = '../model/data/train/imgs'

imgs = [f for f in listdir(IMGS_PATH) if isfile(join(IMGS_PATH, f))]
labels = [f for f in listdir(LABELS_PATH) if isfile(join(LABELS_PATH, f))]

imgs_with_labels = []

# removing duplicate labels
labels = list(dict.fromkeys(labels))

# getting images that have corresponding labels
for img in imgs:
    label = img.split('.')[0] + '.txt'
    if label in labels:
        imgs_with_labels.append(img)

# copying these images to a new folder
for img in imgs_with_labels:
    shutil.copy(join(IMGS_PATH, img), NEW_IMG_PATH)