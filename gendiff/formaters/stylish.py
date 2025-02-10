#from gendiff.scripts.generate_diff1 import generate_dif


def format_diff(diff, depth=0, format_name='stylish'):
    if format_name == 'stylish':
        indent = "  " * depth
        result = []
        
        for key, value in sorted(diff.items()):
            action = value.get("action")
            
            if action == "nested":
                result.append(f"{indent}{key}: {{")
                result.append(format_diff(value["children"], depth + 1))
                result.append(f"{indent}}}")
            elif action == "unchange":
                result.append(f"{indent}  {key}: {format_value(value['value'], depth + 1)}")
            elif action == "add":
                result.append(f"{indent}+ {key}: {format_value(value['value'], depth + 1)}")
            elif action == "remove":
                result.append(f"{indent}- {key}: {format_value(value['value'], depth + 1)}")
            elif action == "change":
                result.append(f"{indent}- {key}: {format_value(value['old_value'], depth + 1)}")
                result.append(f"{indent}+ {key}: {format_value(value['new_value'], depth + 1)}")
        
        return "\n".join(result)

def format_value(value, depth):
    indent = "  " * depth
    if isinstance(value, dict):
        formatted = "{\n" + "\n".join(f"{indent}  {k}: {format_value(v, depth + 1)}" for k, v in value.items()) + f"\n{indent}}}"
        return formatted
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)
