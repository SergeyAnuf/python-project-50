

def format_value(value):
    """Format a value for display, handling complex values."""
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def process_changes(diff, parent_key=""):
    """Recursively process the changes and generate the output."""
    output = []
    for key, values in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        action = values.get("action")

        if action == "nested":
            output.extend(process_changes(values["children"], current_key))
        elif action == "add":
            value = format_value(values["value"])
            output.append(f"Property '{current_key}' was added with value: {value}")
        elif action == "remove":
            output.append(f"Property '{current_key}' was removed")
        elif action == "change":
            old_value = format_value(values["old_value"])
            new_value = format_value(values["new_value"])
            output.append(f"Property '{current_key}' was updated. "
            f"From {old_value} to {new_value}")
        elif action == "unchange":
            value = format_value(values["value"])
            output.append(f"Property '{current_key}' unchange. Was value: {value}")
    
    return output



