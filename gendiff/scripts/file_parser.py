import json

import yaml


def parser_file(file1_path, file2_path):
    try:
        with open(file1_path) as f1, open(file2_path) as f2:
            if file1_path.endswith('json') and file2_path.endswith('json'):
                file_1_dict = json.load(f1)
                file_2_dict = json.load(f2)
            elif file1_path.endswith('yaml' or 'yml') and file2_path.endswith('yaml' or 'yml'):
                file_1_dict = yaml.safe_load(f1)
                file_2_dict = yaml.safe_load(f2)
        return file_1_dict, file_2_dict
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return {}, {}
