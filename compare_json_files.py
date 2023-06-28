from utils import *

"""
Compare two json files by keys in dictionaris
"""

filepath = 'data/compare_two_json_file'

json1 = f'{filepath}/file1.json'
json2 = f'{filepath}/file2.json'

file1 = load_json_file(json1)
file2 = load_json_file(json2)


def compare(differents_dict, file1, file2):
    for key1, value1 in file1.items():
        for key2, value2 in file2.items():
            if key1 == key2:
                if type(value1) == dict:
                    compare(differents_dict, value1, value2)
                elif type(value1) == list:
                    for el in range(0, len(value1)):
                        differents_dict[f"{key1}_{el}"] = {}
                        compare(differents_dict[f"{key1}_{el}"], value1[el], value2[el])
                else:
                    if value1 != value2:
                        differents_dict[key1] = (value1, value2)
    return differents_dict


result = compare({}, file1, file2)
print(result)

save_json_to_file(f"{filepath}/differents_to_file.json", result)
