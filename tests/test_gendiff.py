from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff import generate_dif



def test_gendif():
    result = '- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: True\n'
    file1_path = 'tests/fixtures/file1.json'
    file2_path = 'tests/fixtures/file2.json'
    file1 = parser_file(file1_path)
    file2 = parser_file(file2_path)
    diff = generate_dif(file1, file2)

    assert diff == result
