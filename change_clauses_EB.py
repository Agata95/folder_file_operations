import glob
import json
import os
import random
import re
import traceback

# Zmiana klauzuli w requestach
# Nowa klauzula w tariff_request2

folder = glob.glob('data/tariff_request/*', recursive=True)


# folder = r'C:\Users\weltag1\PycharmProjects\folder_file_operations\data\tariff_request\\'
# dirs = os.listdir(folder)

def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


table_value = [
    "002KBO/S50;S51;S52;S53/v.1",
    None,
    "292341",
    "Klauzula braku odpowiedzialności",
    None,
    "true",
    None,
    "NONE",
    None,
    None,
    None,
    None,
    "NONE",
    None,
    None,
    None,
    "0",
    None,
    "false",
    None
]


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
            for att in risk['attributeList']:
                if att['symbol'] == 'Clauses':
                    att['tableValue'] = [table_value]
                    print(att['tableValue'])

        for partner in pol['partnerList']:
            print(partner['businessPartner']['organizationData']['regon'])
            partner['businessPartner']['organizationData']['regon'] = f'{round_number(9)}'
            print(partner['businessPartner']['organizationData']['regon'])
            print(partner['businessPartner']['organizationData']['nip'])
            partner['businessPartner']['organizationData']['nip'] = f'{round_number(10)}'
            print(partner['businessPartner']['organizationData']['nip'])

    filepath = fr'data\tariff_request2\{os.path.basename(file)}'
    with open(filepath, 'w', encoding='utf_8-sig') as f:
        json.dump(request, f, indent=2, ensure_ascii=False)

