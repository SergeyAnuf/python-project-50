import pytest
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.stylish import format_diff
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff

def test_gendiff():
    file1_dict = {
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

    file2_dict = {
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
