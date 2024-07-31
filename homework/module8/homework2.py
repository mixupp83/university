def add_everything_up(a, b):
    # Проверка на разные типы
    if (isinstance(a, (int, float)) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, (int, float))):
        return str(a) + str(b)

    # Если оба числа или обе строки
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))  # яблоко4215
print(add_everything_up(123.456, 7))  # 130.456