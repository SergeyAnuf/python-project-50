from gendiff.formatters.format_identifier import format_identifier
from gendiff.scripts.find_diff import find_diff
from gendiff.scripts.parser import parse_data_from_file


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse_data_from_file(file_path1)
    file2 = parse_data_from_file(file_path2)
    diff = find_diff(file1, file2)
    return format_identifier(diff, formatter)