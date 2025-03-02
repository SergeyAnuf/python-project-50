def format_diff(diff, depth=0, format_name='stylish'):
    """Форматирует diff в стиль 'stylish'."""
    if format_name == 'stylish':
        indent = "    " * depth  # Увеличил отступ для лучшего форматирования
        result = ["{"]  # Начинаем с открывающей скобки

        for key, value in sorted(diff.items()):
            action = value.get("action")

            if action == "nested":
                result.append(f"{indent}    {key}: {format_diff(value['children'], depth + 1)}")
            elif action == "unchanged":
                result.append(f"{indent}    {key}: {format_value(value['value'], depth + 1)}")
            elif action == "added":
                result.append(f"{indent}  + {key}: {format_value(value['value'], depth + 1)}")
            elif action == "removed":
                result.append(f"{indent}  - {key}: {format_value(value['value'], depth + 1)}")
            elif action == "changed":
                result.append(f"{indent}  - {key}: {format_value(value['old_value'], depth + 1)}")
                result.append(f"{indent}  + {key}: {format_value(value['new_value'], depth + 1)}")

        result.append(f"{indent}}}")  # Закрываем блок
        return "\n".join(result)


def format_value(value, depth):
    """Форматирование значений с правильными отступами."""
    indent = "    " * depth  # 4 пробела для отступа

    if isinstance(value, dict):
        formatted = (
            "{\n"
            + "\n".join(
                f"{indent}    {k}: {format_value(v, depth + 1)}"
                for k, v in value.items()
            )
            + f"\n{indent}}}"
        )
        return formatted
    if value is None:
        return "null"  # ✅ JSON-формат null
    if isinstance(value, bool):
        return "true" if value else "false"  # ✅ JSON-формат true/false
    if isinstance(value, str):
        return f"'{value}'"  # ✅ Добавляем кавычки для строк!
    return str(value)
