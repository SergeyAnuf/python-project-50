def format_value(value):
    """Format a value for display, handling complex values."""
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def process_changes(diff, parent_key=""):
    output = []
    for key, values in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        action = values.get("action")

        if action == "nested":
            output.extend(process_changes(values["children"], current_key))
        elif action == "added":
            value = format_value(values["value"])
            output.append(f"Property '{current_key}' was added with value: {value}")
        elif action == "removed":
            output.append(f"Property '{current_key}' was removed")
        elif action == "changed":
            old_value = format_value(values["old_value"])
            new_value = format_value(values["new_value"])
            output.append(f"Property '{current_key}' was updated. From {old_value} to {new_value}")
        elif action == "unchanged":
            value = format_value(values["value"])
            output.append(f"Property '{current_key}' remained unchanged. Value: {value}")

    return output
