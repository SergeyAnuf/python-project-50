import argparse

from gendiff.formaters.stylish import format_diff
from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate diff between two files.')
parser.add_argument('file1', type=str, help='Path to the first file')
parser.add_argument('file2', type=str, help='Path to the second file')
parser.add_argument('--format', type=str, default='stylish', choices=['stylish', 'plain', 'json'],
                    help='Output format (stylish, plain, json)')
args = parser.parse_args()

file1_path = args.file1
file2_path = args.file2

# Read and parse files
with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
    file1 = f1.read()
    file2 = f2.read()
    file_1_dict, file_2_dict = parser_file(file1, file2)

# Generate diff
diff = generate_dif(file_1_dict, file_2_dict)

# Format the diff based on the specified format
if args.format == 'plain':
    result = process_changes(diff)
    file_result_path = 'file_result_plain.txt'
elif args.format == 'json':
    result = transform_diff(diff)
    file_result_path = 'result_test_json.txt'
else:
    result = format_diff(diff)
    file_result_path = 'file_result.txt'

# Write the result to the file
with open(file_result_path, 'w') as f:
    f.write(result)

# Read the result back from the file for comparison
with open(file_result_path, 'r') as f:
    result_test = f.read()

# Assert that the result matches the expected output
assert result_test == result, "The result does not match the expected output."

print("Diff generated successfully and matches the expected output.")
