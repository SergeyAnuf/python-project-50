def generate_dif(file_1_dict, file_2_dict):
    diff = ''
    file_1_dict = dict(sorted(file_1_dict.items()))

    for key, value in file_1_dict.items():
        if key not in file_2_dict:
            diff += f' - {key}: {value}\n'
        elif file_1_dict[key] == file_2_dict[key]:
            diff += f'   {key}: {value}\n'
        else:
            diff += f' - {key}: {file_1_dict[key]}\n + {key}: {file_2_dict[key]}\n' 

    for key, value in file_2_dict.items():
        if key not in file_1_dict:
            diff += f' + {key}: {value}\n'

    return diff
