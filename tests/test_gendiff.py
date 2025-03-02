import pytest

from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.parser import read_file


@pytest.mark.parametrize('file_path1, file_path2, expected_result', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_result_json.txt'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_result_yaml.txt')])
def test_generate_diff(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2)
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected


@pytest.mark.parametrize('file_path1, file_path2, expected_result', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_result_plain.txt'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_result_plain.txt')])
def test_generate_diff_plain(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2, formatter="plain")
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected


@pytest.mark.parametrize('file_path1, file_path2, expected_result', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'tests/fixtures/expected_result_json_format.txt'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/expected_result_json_format.txt')])
def test_generate_diff_json(file_path1, file_path2, expected_result):
    diff = generate_diff(file_path1, file_path2, formatter="json")
    expected = read_file(expected_result).strip()
    assert diff.strip() == expected
