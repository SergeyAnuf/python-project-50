import json

def parser_file(file1_path, file2_path):
    try:
        with open(file1_path) as f1, open(file2_path) as f2:
            file_1_dict = json.load(f1)
            file_2_dict = json.load(f2)
        return file_1_dict, file_2_dict
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return {}, {}

