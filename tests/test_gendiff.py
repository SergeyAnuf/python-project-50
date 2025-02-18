import argparse

from gendiff.formaters.stylish import format_diff
from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff

parser.add_argument("-f", "--format", help="Формат вывода", default="stylish" , choices=['stylish', 'plain', 'json'])

    # Разбираем аргументы
args = parser.parse_args()

    # Загружаем файлы
file_1_dict, file_2_dict = parser_file(args.first_file, args.second_file)

    # Генерируем разницу
diff = generate_dif(file_1_dict, file_2_dict)
    
    # Форматируем разницу
if args.format == 'plain':
    result = process_changes(diff)
    file_result_path = 'tests/fixtures/file_result_plain.txt'
    with open(file_result_path, 'r') as f5:
        result_test = f5.read()
        
elif args.format == 'json':
    transformed_diff = transform_diff(diff)
    result = json.dumps(transformed_diff, indent = 4)
    file_result_path = 'tests/fixtures/result_test.json'
    with open(file_result_path, 'r') as f:
        result_test = f.read()

else:
    result = format_diff(diff)
    file_result_path = 'tests/fixtures/file_result.txt'
    with open(file_result_path, 'r') as f5:
        result_test = f5.read()
        
assert result_test == result
