import json

def parser_file():
    file_1_dict = json.load(open('/home/sergey/python-project-50/file1.json'))
    file_2_dict = json.load(open('/home/sergey/python-project-50/file2.json'))
    return file_1_dict, file_2_dict
