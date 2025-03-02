import argparse

from gendiff.scripts.generate_diff import generate_diff


def parser_function():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", "--format",
                        help='set format of output',
                        default='stylish', type=str
    )

    return parser.parse_args()


def main():
    args = parser_function()

    file_path1 = args.first_file
    file_path2 = args.second_file

    result = generate_diff(file_path1, file_path2, formatter=args.format)
    print(result)


if __name__ == "__main__":
    main()