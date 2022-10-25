"""
    Program to fetch a subset of labels for given images from a directory of all labels

    img_dir_1 = {img1.jpg, img2.jpg, img3.jpg}
    label_dir_1 = {}
    label_dir_2 = {img1.txt, img2.txt, img3.txt, img4.txt, img5.txt}
    ==================================================================
    img_dir_1 = {img1.jpg, img2.jpg, img3.jpg} *
    label_dir_1 = {img1.txt, img2.txt, img3.txt} *
    label_dir_2 = {img1.txt, img2.txt, img3.txt, img4.txt, img5.txt}
"""

from os import listdir
from os.path import isfile, join
import shutil

IMGS_PATH = '../cattle-data/c3_imgs'
LABELS_PATH = '../cattle-data/c3_master/train/labels'
NEW_LABELS_PATH = '../cattle-data/c3_labels'

imgs = [f for f in listdir(IMGS_PATH) if isfile(join(IMGS_PATH, f))]
labels = [f for f in listdir(LABELS_PATH) if isfile(join(LABELS_PATH, f))]

labels_with_imgs = []

for img in imgs:
    label = img[:-4] + '.txt'
    if label in labels:
        labels_with_imgs.append(label)

print(len(imgs), 'images found.')
print(len(labels_with_imgs), 'corresponding labels found ')

# copying these images to a new folder
for label in labels_with_imgs:
    shutil.copy(join(LABELS_PATH, label), NEW_LABELS_PATH)

print('Labels moved to new destination successfully!')


