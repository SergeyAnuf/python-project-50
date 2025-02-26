

def generate_diff(file_1_dict, file_2_dict):
    diff = {}
    for key, value in file_2_dict.items():
        if key in file_1_dict:
            if isinstance(value, dict):
                children1 = file_1_dict[key]
                children2 = file_2_dict[key]
                diff[key] = {
                    'action': 'nested',
                    'children': generate_dif(children1, children2)
                }
            else:
                if file_2_dict[key] == file_1_dict[key]:
                    diff[key] = {'action': 'unchange', 'value': value}
                elif file_2_dict[key] != file_1_dict[key]:
                    diff[key] = {'action': 'change',
                    'old_value': file_1_dict[key], 'new_value': file_2_dict[key]
                }
        elif key not in file_1_dict:
            diff[key] = {'action': 'add', 'value': value}
    for key, value in file_1_dict.items():
        if key not in file_2_dict:
            diff[key] = {'action': 'remove', 'value': value}

    return diff



