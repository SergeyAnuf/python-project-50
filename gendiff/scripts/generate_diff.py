from gendiff.scripts.file_parser import parser_file


def generate_diff(file1_path, file2_path):
    file_1_dict, file_2_dict = parser_file(file1_path, file2_path)
    diff = {}

    all_keys = sorted(set(file_1_dict) | set(file_2_dict))

    for key in all_keys:
        old_value = file_1_dict.get(key)
        new_value = file_2_dict.get(key)

        if key not in file_1_dict:
            diff[key] = {"action": "added", "value": new_value}
        elif key not in file_2_dict:
            diff[key] = {"action": "removed", "value": old_value}
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            diff[key] = {"action": "nested", "children": generate_diff_from_dicts(old_value, new_value)}
        elif old_value != new_value:
            diff[key] = {"action": "changed", "old_value": old_value, "new_value": new_value}
        else:
            diff[key] = {"action": "unchanged", "value": old_value}

    return diff


def generate_diff_from_dicts(dict1, dict2):
    diff = {}

    all_keys = sorted(set(dict1) | set(dict2))

    for key in all_keys:
        old_value = dict1.get(key)
        new_value = dict2.get(key)

        if key not in dict1:
            diff[key] = {"action": "added", "value": new_value}
        elif key not in dict2:
            diff[key] = {"action": "removed", "value": old_value}
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            diff[key] = {"action": "nested", "children": generate_diff_from_dicts(old_value, new_value)}
        elif old_value != new_value:
            diff[key] = {"action": "changed", "old_value": old_value, "new_value": new_value}
        else:
            diff[key] = {"action": "unchanged", "value": old_value}

    return diff
