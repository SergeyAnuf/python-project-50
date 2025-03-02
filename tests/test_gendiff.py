import json

from gendiff.formaters.formater_json import transform_diff
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.stylish import format_diff
from gendiff.scripts.generate_diff import generate_diff


def test_gendiff():
    file1_path = 'tests/fixtures/file3.json'
    file2_path = 'tests/fixtures/file4.json'

    diff = generate_diff(file1_path, file2_path)

    result_stylish = format_diff(diff)
    result_plain = process_changes(diff)
    result_json = transform_diff(diff)

    with open('tests/fixtures/file_result.txt', 'r') as f1:
        expected_stylish = f1.read().strip()

    with open('tests/fixtures/file_result_plain.txt', 'r') as f2:
        expected_plain = f2.read().strip()

    with open('tests/fixtures/result_test_json.txt', 'r', encoding='utf-8') as f3:
        expected_json = json.loads(f3.read().strip())
    print("\n".join(result_plain))
    print("----")
    print(expected_plain)
    print(json.dumps(result_json, indent=4))  # Вывод актуального JSON
    print("----")
    print(json.dumps(expected_json, indent=4))  # Вывод эталонного JSON

    assert result_stylish == expected_stylish
    assert "\n".join(result_plain) == expected_plain
    assert result_json == expected_json
