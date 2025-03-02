import json
import yaml
from gendiff.formaters.formater_json import transform_diff
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.stylish import format_diff
from gendiff.scripts.generate_diff import generate_diff

def test_gendiff():
    for file1_path, file2_path in [
        ('tests/fixtures/file3.json', 'tests/fixtures/file4.json'),
        ('tests/fixtures/file3.yaml', 'tests/fixtures/file4.yaml'),
    ]:
        diff = generate_diff(file1_path, file2_path)

        result_stylish = format_diff(diff)
        result_plain = process_changes(diff)
        result_json = transform_diff(diff)

        with open('tests/fixtures/file_result.txt', 'r') as f1:
            expected_stylish = f1.read().strip()

        with open('tests/fixtures/file_result_plain.txt', 'r') as f2:
            expected_plain = f2.read().strip()

        with open('tests/fixtures/result_test_json.txt', 'r', encoding='utf-8') as f3:
            expected_json = json.load(f3)

        assert result_stylish == expected_stylish
        assert "\n".join(result_plain) == expected_plain
        assert result_json == expected_json
