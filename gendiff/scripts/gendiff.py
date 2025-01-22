import argparse
from generate_diff import generate_dif
from file_parser import parser_file

parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference."
)
parser.add_argument("fist_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()

def main():
    file_1_dict, file_2_dict = parser_file()
    diff = generate_dif(file_1_dict, file_2_dict)
    print(diff)

if __name__ == "__main__":
    main()




