import pytest
from gendiff.scripts.generate_diff1 import generate_dif
from gendiff.formaters.stylish import format_diff
from gendiff.formaters.formater_plain import process_changes
from gendiff.formaters.formater_json import transform_diff

def test_gendiff():
    file_1_dict = {
      "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
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

    file_2_dict = {
      "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
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
    
    file_result = 'file_result.txt'
    with open(file_result, 'r') as f1:
        result1 = f1.read()
    
    file_result_plain = 'tests/fixtures/file_result_plain.txt'
    with open(file_result_plain, 'r') as f2:
        result2 = f2.read()
        
    file_result_json = 'tests/fixtures/result_test_json.txt'
    with open(file_result_json, 'r') as f3:
        result3 = f3.read()

    assert result_stylish == result1
    assert result_plain == result2
    assert result_json == result3
