from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff import generate_dif



def test_gendif():
    result = '- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n'
    file1 = {"host": "hexlet.io", "timeout": "50", "proxy": "123.234.53.22", "follow": "False"}
    file2 = {"timeout": "20", "verbose": "True", "host": "hexlet.io"}
    diff = generate_dif(file1, file2)

    assert diff == result
