import json


def load_json_file(filename):
    try:
        with open(f"{filename}", encoding='utf_8-sig') as json_file:
            return json.load(json_file)
    except Exception as ex:
        print(f'ERROR {filename}: {ex}')
        return {}


def save_json_to_file(filepath, file_to_save):
    try:
        with open(f"{filepath}", 'w', encoding='utf_8-sig') as json_file:
            json.dump(file_to_save, json_file, indent=2, ensure_ascii=False)
    except Exception as ex:
        print(f'ERROR {filepath}: {ex}')
