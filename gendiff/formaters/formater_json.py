import json


def transform_diff(diff):
    """
    Рекурсивно преобразует diff в нужный формат.
    """
    result = {}
    for key, value in diff.items():
        action = value['action']
        if action == 'nested':
            # Для вложенных значений рекурсивно вызываем функцию
            result[key] = ['nested', transform_diff(value['children'])]
        elif action == 'add':
            # Для добавленных значений
            result[key] = ['added', value['value']]
        elif action == 'remove':
            # Для удалённых значений
            result[key] = ['removed', value['value']]
        elif action == 'unchange':
            # Для неизменённых значений
            result[key] = ['unchanged', value['value']]
        elif action == 'change':
            # Для изменённых значений
            result[key] = ['changed', [value['old_value'], value['new_value']]]
    return result


def save_diff_to_json(diff, output_file):
    """
    Сохраняет diff в JSON-файл.
    """
    transformed_diff = transform_diff(diff)
    with open(output_file, 'w') as f:
        json.dump(transformed_diff, f, indent=4)
