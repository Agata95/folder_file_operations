import glob
import json
import os
import random
import re
import traceback

# skrypt szuka w podanych responsach, konkretnych responsów z podanymi warunkami
# --WARUNKI:
# --umowę generalną, partnerList mają wyłącznie osoby lub jdg
# --warunek na response: premiumchangeallowed na ryzyku OC musi być na true i na tym samym ryzyku calculationAlgorithm musi być NONE

folder_res = glob.glob('data/tariff_request/*', recursive=True)


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


for res in folder_res:
    response = load_json_file(res)

    policy = response['root']['applicationList'][0]['policyList']

    for pol in policy:
        for partner in pol['partnerList']:
            try:
                for doc in partner['businessPartner']['personData']['identityDocumentList']:
                    if not 'documentNumber' in doc.keys():
                        print(os.path.basename(res))
            except:
                pass
