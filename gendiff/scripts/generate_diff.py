from gendiff.scripts.file_parser import parser_file


def generate_diff(file1_path, file2_path):
    file_1_dict, file_2_dict = parser_file(file1_path, file2_path)  # Загружаем файлы
    diff = {}

    for key, value in file_2_dict.items():  # Теперь file_2_dict точно словарь
        if key not in file_1_dict:
            diff[key] = {"status": "added", "value": value}
        elif file_1_dict[key] != value:
            diff[key] = {"status": "changed", "old_value": file_1_dict[key], "new_value": value}
        else:
            diff[key] = {"status": "unchanged", "value": value}

    for key in file_1_dict:
        if key not in file_2_dict:
            diff[key] = {"status": "removed", "value": file_1_dict[key]}

    return diff
