"""
    Program to change labels for a directory of images to point to a new class

    WARNING - this is a mutating program, meaning it will change your files. Take a backup
    before running this script

    POST-RUNNING - change the classes.txt accordingly in your main labels folder after execution
    of this script
"""

from os import listdir
from os.path import isfile, join

LABELS_PATH = '../cattle-data/labels'
NEW_CLASS = '1'

labels = [f for f in listdir(LABELS_PATH) if isfile(join(LABELS_PATH, f))]

for label in labels:
    file = open(join(LABELS_PATH, label), "r+")
    contents = file.read().strip().split('\n')
    new_contents = ''

    for entry in contents:
        new_contents += NEW_CLASS + entry[1:] + '\n'

    file.seek(0)
    file.truncate()
    file.write(new_contents)

    file.close()

print('Edited', len(labels), 'files successfully!')