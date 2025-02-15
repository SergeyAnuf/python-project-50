import argparse

from gendiff.formaters.stylish import format_diff
from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff


def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Добавляем аргументы для файлов
    parser.add_argument("first_file", help="Первый файл для сравнения")
    parser.add_argument("second_file", help="Второй файл для сравнения")

    # Опциональный аргумент для формата вывода (необязательный)
    parser.add_argument("-f", "--format", help="Формат вывода", default="stylish" , choices=['stylish', 'plain'])

    # Разбираем аргументы
    args = parser.parse_args()

    # Загружаем файлы
    file_1_dict, file_2_dict = parser_file(args.first_file, args.second_file)

    # Генерируем разницу
    diff = generate_dif(file_1_dict, file_2_dict)
    
    # Форматируем разницу
    if args.format == 'plain':
        result = process_changes(diff)
        for line in result:
            print(line)
    elif args.format == 'json':
        result = transform_diff(diff)
    else:
        result = format_diff(diff)
        print(result)   
    


if __name__ == "__main__":
    main()




