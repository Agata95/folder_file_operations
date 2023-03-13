import glob
import json
import os
import re

folder_one = glob.glob('data/e_one/*', recursive=True)
folder_two = glob.glob('data/e_two/*', recursive=True)


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


for file_one in folder_one:
    for file_two in folder_two:
        file_1 = load_json_file(file_one)
        file_2 = load_json_file(file_two)

        print(file_1['salesTransactionId'])
        print(file_2['salesTransactionId'])
        print("==============================")

        # if file_1['salesTransactionId'] == file_2['salesTransactionId']:
        #     print(os.path.basename(file_one), os.path.basename(file_two))
        #     print("----")