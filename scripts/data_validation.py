from os import listdir
from os.path import isfile, join

IMGS_PATH = '../cattle-data/images'
LABELS_PATH = '../cattle-data/labels'
SHOW_UNMATCHED_IMGS = False

imgs = [f for f in listdir(IMGS_PATH) if isfile(join(IMGS_PATH, f))]
labels = [f for f in listdir(LABELS_PATH) if isfile(join(LABELS_PATH, f))]

if len(imgs) != len(labels):
    print('Number of images and labels do not match')
    print('Images:',len(imgs))
    print('Labels:',len(labels))
else:
    print('Number of images match the number of labels')

count = 0
non_matches = []
for img in imgs:
    label = imgs[0][:-4] + '.txt'
    if label not in labels:
        count += 1
        non_matches.append(img)

if count == 0:
    print('All images have corresponding labels')
else:
    print(count,'images do not have correspinding labels')
    if SHOW_UNMATCHED_IMGS:
        print('Unmatched images:',non_matches)