import json

import yaml


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        if file_path.endswith('.json'):
            return json.load(f)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported file format")


def parser_file(file1_path, file2_path):
    return load_file(file1_path), load_file(file2_path)
