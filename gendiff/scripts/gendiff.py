import argparse

parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()
file_path1, file_path2
[](url)
from generate_diff import generate_dif

diff = generate_dif(file_1_dict, file_2_dict)
print(diff)


if __name__ == "__main__":
    main()[](url)
