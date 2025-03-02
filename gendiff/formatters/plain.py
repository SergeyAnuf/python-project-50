def format_value(value):
    if isinstance(value, (dict, list)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def make_plain_item(item, path=''):
    key = item.get('name')
    action = item.get('action')
    new_value = format_value(item.get('new_value'))
    old_value = format_value(item.get('old_value'))
    current_path = f"{path}.{key}" if path else key

    ADD = ' was added with value: '
    REMOVE = ' was removed'
    UPD = ' was updated. From '
    UPD2 = ' to '
    PROP = 'Property '

    if action == 'added':
        return f"{PROP}'{current_path}'{ADD}{new_value}"
    if action == 'deleted':
        return f"{PROP}'{current_path}'{REMOVE}"
    if action == 'modified':
        return f"{PROP}'{current_path}'{UPD}{old_value}{UPD2}{new_value}"
    if action == 'nested':
        children = item.get('children')
        return make_plain_diff(children, current_path)
    return None


def make_plain_diff(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(diff):
    return make_plain_diff(diff)