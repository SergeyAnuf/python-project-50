import argparse

from gendiff.formaters.stylish import format_diff
from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff
from gendiff.scripts.gendiff import main

file1_path = 'file3.json'
file2_path = 'file4.json'
with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
    file1 = f1.read()
    file2 = f2.read()
    file_1_dict, file_2_dict = parser_file(file1, file2)

diff = generate_dif(file_1_dict, file_2_dict)
    
    # Форматируем разницу
if args.format == 'plain':
    result = process_changes(diff)
    file_result_path = 'file_result_plain.txt'
    with open(file_result_path, 'r') as f5:
        result_test = f5.read()
        
elif args.format == 'json':
    result = transform_diff(diff)
    file_result_path = 'result_test_json.txt'
    with open(file_result_path, 'r') as f:
        result_test = f.read()

else:
    result = format_diff(diff)
    file_result_path = 'file_result.txt'
    with open(file_result_path, 'r') as f5:
        result_test = f5.read()
        
assert result_test == result
