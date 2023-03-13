import glob
import os

folder_one = glob.glob('data/iHestia/*', recursive=True)
folder_two = glob.glob('data/iHestia-req/*', recursive=True)

for file_one in folder_one:
    for file_two in folder_two:
        if os.path.basename(file_one) == os.path.basename(file_two):
            os.remove(file_one)

