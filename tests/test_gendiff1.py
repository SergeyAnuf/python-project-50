import json

import yaml

from gendiff.scripts.generate_diff1 import generate_dif


def test_gendif1_json():
    file3_path = 'tests/fixtures/file3.json'
    file4_path = 'tests/fixtures/file4.json'
    file_result_path = '/home/sergey/python-project-50/tests/fixtures/file_result.txt'
    with open(file_result_path, 'r') as f5:
        result = f5.read()
    with open(file3_path) as f3, open(file4_path) as f4:
        file_1_dict = json.load(f3)
        file_2_dict = json.load(f4)
    diff = generate_dif(file_1_dict, file_2_dict)

    assert diff == result
    
    
def test_gendif1_yaml():
    file3_path = 'tests/fixtures/file3.yaml'
    file4_path = 'tests/fixtures/file4.yaml'
    file_result_path = '/home/sergey/python-project-50/tests/fixtures/file_result.txt'
    with open(file_result_path, 'r') as f5:
        result = f5.read()
    with open(file3_path) as f3, open(file4_path) as f4:
        file_1_dict = yaml.safe_load(f1)
        file_2_dict = yaml.safe_load(f2)
    diff = generate_dif(file_1_dict, file_2_dict)

    assert diff == result
