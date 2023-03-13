import glob
import json
import os
import random
import re
import traceback

folder = glob.glob('data/tariff_request/*', recursive=True)


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


def round_number(numbers):
    random_num = random.sample(range(0, 10), numbers)
    string = ''
    for el in random_num:
        string += str(el)
    return string


for file in folder:
    request = load_json_file(file)

    policy = request['root']['applicationList'][0]['policyList']

    for pol in policy:
        for risk in pol['riskList']:
            if risk['productData']['id'] == 'HCA_PREMIUM' or risk['productData']['id'] == 'HCA_PRESTIZ':
                risk['calculationAlgorithm'] = 'EARNIX'

    filepath = fr'data\tariff_request2\{os.path.basename(file)}'
    with open(filepath, 'w', encoding='utf_8-sig') as f:
        json.dump(request, f, indent=2, ensure_ascii=False)

