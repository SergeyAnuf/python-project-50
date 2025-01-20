from file_parser import parser_file


def generate_dif(file_1_dict, file_2_dict):

    diff = ''
    file_1_dict = dict(sorted(file_1_dict.items()))
    for key, value in file_1_dict.items():
        if key not in file_2_dict:
            diff = diff + f'- {key}: {value}\n'
        elif key in file_2_dict and file_1_dict[key] == file_2_dict[key]:
            diff = diff + f'  {key}: {value}\n'
        elif key in file_2_dict and file_1_dict[key] != file_2_dict[key]:
            diff = diff + f'- {key}: {file_1_dict[key]}\n+ {key}: {file_2_dict[key]}\n'
    for key, value in file_2_dict.items():
        if key not in file_1_dict:
            diff = diff + f'+ {key}: {value}\n'

    return diff
    
file_1_dict, file_2_dict = parser_file()
#generate_dif(file_1_dict, file_2_dict)
