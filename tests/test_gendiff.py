from gendiff.scripts.generate_diff import generate_dif
import json
import yaml


def test_gendif(file1_path, file2_path):
    result = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n'
    '+ timeout: 20\n+ verbose: true\n'
    with open(file1_path) as f1, open(file2_path) as f2:
        if f1.endswith('json') and f2.enswith('json'):
            file_1_dict = json.load(f1)
            file_2_dict = json.load(f2)
        elif f1.endswith('yaml' or 'yml') and f2.enswith('yaml' or 'yml'):
            file_1_dict = yaml.safe_load(f1)
            file_2_dict = yaml.safe_load(f2)
    diff = generate_dif(file_1_dict, file_2_dict)

    assert diff == result
