from generate_diff1 import generate_dif

diff = generate_dif()

def format_diff(diff, depth=0):
    indent = ' ' * (4 * depth)
    result = '{\n'
    for key, value in diff.items():
        action = value.get('action')

        # ?????????? ??????? ??? ???????? ??????
        current_indent = ' ' * (4 * (depth + 1))

        if action == 'nested':
            # ?????????? ???????????? ????????? ????????
            nested_diff = format_diff(value['children'], depth + 1)
            result += f'{current_indent}{key}: {nested_diff}\n'

        elif action == 'unchange':
            result += f'{current_indent}{key}: {value["value"]}\n'

        elif action == 'change':
            result += f'{current_indent}- {key}: {value["old_value"]}\n'
            result += f'{current_indent}+ {key}: {value["new_value"]}\n'

        elif action == 'add':
            result += f'{current_indent}+ {key}: {value["value"]}\n'

        elif action == 'remove':
            result += f'{current_indent}- {key}: {value["value"]}\n'

    result += f'{indent}}}'
    return result

# ??????? ????????????????? diff
formatted_diff = format_diff(diff)
print(formatted_diff)
