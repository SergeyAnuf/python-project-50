import pytest
from gendiff.scripts.file_parser import parser_file
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.stylish import format_diff
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff

def parse_args():
    """
    Parse command-line arguments for testing.
    """
    import argparse
    parser = argparse.ArgumentParser(description='Generate diff between two files.')
    parser.add_argument('file1', type=str, help='Path to the first file')
    parser.add_argument('file2', type=str, help='Path to the second file')
    parser.add_argument('--format', type=str, default='stylish', choices=['stylish', 'plain', 'json'],
                        help='Output format (stylish, plain, json)')
    return parser.parse_args()

def test_gendiff():
    # Mock file content for testing
    file1_content = '''
    {
      "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": true,
        "setting6": {
          "key": "value",
          "doge": {
            "wow": ""
          }
        }
      },
      "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
          "key": "value"
        }
      },
      "group2": {
        "abc": 12345,
        "deep": {
          "id": 45
        }
      }
    }
    '''
    file2_content = '''
    {
      "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": true,
        "setting6": {
          "key": "value",
          "doge": {
            "wow": ""
          }
        }
      },
      "group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
          "key": "value"
        }
      },
      "group2": {
        "abc": 12345,
        "deep": {
          "id": 45
        }
      }
    }
    '''

    # Parse file content into dictionaries
    file_1_dict, file_2_dict = parser_file(file1_content, file2_content)

    # Generate diff
    diff = generate_dif(file_1_dict, file_2_dict)

    # Test different formats
    result_stylish = format_diff(diff)
    result_plain = process_changes(diff)
    result_json = transform_diff(diff)

    # Add assertions here
    assert isinstance(result_stylish, str)
    assert isinstance(result_plain, str)
    assert isinstance(result_json, str)
