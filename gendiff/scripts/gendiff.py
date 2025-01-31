import argparse

from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff import generate_dif


def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    # Добавляем аргументы для файлов
    parser.add_argument("first_file", help="Первый файл для сравнения")
    parser.add_argument("second_file", help="Второй файл для сравнения")

    # Опциональный аргумент для формата вывода (необязательный)
    parser.add_argument("-f", "--format", help="Формат вывода", default="plain")

    # Разбираем аргументы
    args = parser.parse_args()

    # Загружаем файлы
    file_1_dict, file_2_dict = parser_file(args.first_file, args.second_file)

    # Генерируем разницу
    diff = generate_dif(file_1_dict, file_2_dict)

    # Выводим результат
    print(diff)


if __name__ == "__main__":
    main()




