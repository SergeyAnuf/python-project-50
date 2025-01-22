import json

file1_path = '/home/sergey/python-project-50/file1.json'
file2_path = '/home/sergey/python-project-50/file2.json'
def parser_file():
    file_1_dict = dict(json.load(open(file1_path)))
    file_2_dict = dict(json.load(open(file2_path)))
    return file_1_dict, file_2_dict

