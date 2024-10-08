def add_everything_up(a, b):
    try:
        c = a + b
        return f'{c:.3f}'
    except TypeError:
        if isinstance(a, (int, float, str)) and isinstance(b, (int, float, str)):
            c = str(a) + str(b)
            return str(c)
        else:
            return f'Невозможная операция ! Принимаем только INT, FLOAT, STR на входе.'
    
    
# код для проверки задания

print(add_everything_up((678, 'rtu'), 456))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

    # Вывод в консоль:
    # 123.456строка
    # яблоко4215
    # 130.456