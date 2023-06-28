import glob
import json
import os

import numpy as np
import pandas as pd

folder = glob.glob('data/tariff_request/*', recursive=True)

df = pd.read_csv(r'data/person_data.csv', sep="^", header=None)
# zamiana 'nan' na None
df = df.astype(object).replace(np.nan, None)


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


row = 0
for file in folder:
    request = load_json_file(file)

    vin = str(df.values[row][0]) if df.values[row][0] else None
    first_name = str(df.values[row][1]) if df.values[row][1] else None
    last_name = str(df.values[row][2]) if df.values[row][2] else None
    pesel = str(df.values[row][3]) if df.values[row][3] else None
    regon = str(df.values[row][4]) if df.values[row][4] else None

    system = None

    try:
        if request['metadata']['systemName'] == 'SOK':
            system = 'SOK'
    except:
        system = 'NSOK'

    if system == 'SOK':
        request['sok']['vehicle']['vin'] = vin

        party_list = request['sok']['partyList']
        for person in party_list:
            person['partyData']['firstName'] = first_name
            person['partyData']['lastName'] = last_name
            person['partyData']['pesel'] = pesel
            person['partyData']['regon'] = regon


    else:
        policy_list = request['root']['applicationList'][0]['policyList']
        for policy in policy_list:
            partner_list = policy['partnerList']
            for partner in partner_list:
                if partner['businessPartner']['partnerType'] not in ('COMPANY', 'O'):
                    partner['businessPartner']['personData']['firstName'] = first_name
                    partner['businessPartner']['personData']['lastName'] = last_name
                    partner['businessPartner']['personData']['pesel'] = pesel

            vehicle_list = policy['objectList']
            for vehicle in vehicle_list:
                vehicle['vehicle']['vin'] = vin

    row += 1
    filepath = fr'data\tariff_request2\{os.path.basename(file)}'
    with open(filepath, 'w', encoding='utf_8-sig') as f:
        json.dump(request, f, indent=2, ensure_ascii=False)
