import json

import yaml


def load_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            elif file_path.endswith(('.yaml', '.yml')):
                return yaml.safe_load(f)
            else:
                raise ValueError(f"Неподдерживаемый формат файла: {file_path}")
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return {}
    except (json.JSONDecodeError, yaml.YAMLError):
        print(f"Ошибка: Файл {file_path} содержит некорректные данные.")
        return {}


def parser_file(file1_path, file2_path):
    file_1_dict = load_file(file1_path)
    file_2_dict = load_file(file2_path)
    return file_1_dict, file_2_dict
