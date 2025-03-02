SEPARATOR = " "
ADD = '+ '
DEL = '- '
NONE = '  '


def format_value(value, spaces_count=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        result_lines = []
        for key, inner_value in value.items():
            formatted_value = format_value(inner_value, spaces_count + 4)
            result_lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(result_lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def make_stylish_diff(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []
    for item in diff:
        key = item['name']
        action = item['action']
        value = format_value(item.get('value'), spaces_count)
        old_value = format_value(item.get('old_value'), spaces_count)
        new_value = format_value(item.get('new_value'), spaces_count)

        if action == "unchanged":
            lines.append(f"{indent}{NONE}{key}: {value}")
        elif action == "modified":
            lines.append(f"{indent}{DEL}{key}: {old_value}")
            lines.append(f"{indent}{ADD}{key}: {new_value}")
        elif action == "deleted":
            lines.append(f"{indent}{DEL}{key}: {old_value}")
        elif action == "added":
            lines.append(f"{indent}{ADD}{key}: {new_value}")
        elif action == 'nested':
            children = make_stylish_diff(item.get("children"), spaces_count + 4)
            lines.append(f"{indent}{NONE}{key}: {children}")
    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)

    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_diff(data)

