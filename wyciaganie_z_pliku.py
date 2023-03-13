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

folder_res = glob.glob('data/tariff_response/*', recursive=True)

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
            if pol['generalAgreementNumber'] == 'EBMW_FS':
                type_list = [partner['businessPartner']['partnerType'] for partner in pol['partnerList']]
                if 'COMPANY' in type_list:
                    break

                for risk in pol['riskList']:
                    if risk['productData']['symbol'] == 'OC':
                        if risk['isPremiumChangeAllowed'] and risk['calculationAlgorithm'] == 'NONE':
                            print(os.path.basename(res))




