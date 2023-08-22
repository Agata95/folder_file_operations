import pandas as pd

char_to_replace = {
    '"': '',
    ' ': '',
    '': '',
    '.': '',
    ',': '',
    '-': '',
    '–': '',
    '„': '',
    '”': ''
}

diacritics_to_replace = {
    'Ą': 'A',
    'Ć': 'C',
    'Ę': 'E',
    'Ł': 'L',
    'Ń': 'N',
    'Ó': 'O',
    'Ś': 'S',
    'Ż': 'Z',
    'Ź': 'Z'
}

df = pd.read_csv(r'data/wykroczenia.csv', sep=";", header=None)
row = 0

# with open(r'data/wykroczenia_2.csv', 'w') as csvoutput:
#     writer = csv.writer(csvoutput, lineterminator='\n')

test = []
for index, row in df.iterrows():
    name = row[0].translate(str.maketrans(char_to_replace)).upper()
    test.append(name)

df['test'] = test

df.to_csv(r'data/wykroczenia_2.csv', sep=";", header=None, encoding='utf_8-sig')


