import json
import yaml
from gendiff.scripts.generate_diff import generate_dif

def test_gendif_json():
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    result = '- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n'\
    '- timeout: 50\n+ timeout: 20\n+ verbose: True\n'
    with open(file1_path) as f1, open(file2_path) as f2:
        file_1_dict = json.load(f1)
        file_2_dict = json.load(f2)
    diff = generate_dif(file_1_dict, file_2_dict)

    assert diff == result
    
    
def test_gendif_yaml():
    file1_path = 'tests/fixtures/file1.yaml'
    file2_path = 'tests/fixtures/file2.yaml'
    result = '- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n'\
    '- timeout: 50\n+ timeout: 20\n+ verbose: True\n'
    with open(file1_path) as f1, open(file2_path) as f2:
        file_1_dict = yaml.safe_load(f1)
        file_2_dict = yaml.safe_load(f2)
    diff = generate_dif(file_1_dict, file_2_dict)

    assert diff == result
