import os
import re

folder = r'C:\Users\weltag1\PycharmProjects\folder_file_operations\data\response\\'


for file in os.listdir(folder):
    # if 'earnix_res' in file:
    os.rename(folder + file, folder + rf'{file.replace("_", "")[:-14]}_tariff_res.json')
    # os.rename(folder + file, folder + rf'{file.replace("_", "")[:-14]}.json')
#
# for file in os.listdir(folder):
#     os.rename(folder + file, folder + rf'{file[1:]}')

#
# a = "17_tariff_res.json"
# print(a.replace('_', '')[:-14])
# a = "17_earnix_req.json"
# print(a.replace('_', '')[:-14])
# a = "e04.json"
# print(a[1:])
