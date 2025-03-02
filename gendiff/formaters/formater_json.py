import json


def transform_diff(diff):
    result = {}
    for key, value in diff.items():
        action = value["action"]
        if action == "nested":
            result[key] = ["nested", transform_diff(value["children"])]
        elif action == "added":
            result[key] = ["added", value["value"]]
        elif action == "removed":
            result[key] = ["removed", value["value"]]
        elif action == "unchanged":
            result[key] = ["unchanged", value["value"]]
        elif action == "changed":
            result[key] = ["changed", [value["old_value"], value["new_value"]]]
    return result



def save_diff_to_json(diff, output_file):
    """
    Сохраняет diff в JSON-файл.
    """
    transformed_diff = transform_diff(diff)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(transformed_diff, f, indent=4, ensure_ascii=False)

