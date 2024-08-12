
def get_multiplied_digits(number):
    # print(type(number), number, ' Переменная ')
    number_str = str(number)
    # print(type(number_str), number_str, ' Сконвертированная ')
    first = int(number_str[0])
    # print(type(first), first, ' Первая ')
    # print(type(number_str[1:]), number_str[1:], 'Второе число')
    if len(number_str[1:]) < 1: # долбаный выход за пределы списка отнял сутки на его отлов
        return first
    return first * get_multiplied_digits(int(number_str[1:]))


result = get_multiplied_digits(40203)
print(result, '- Результат работы функции с числом "40203"')

result = get_multiplied_digits(123456789)
print(result, '- Результат работы функции с числом "123456789"')

result = get_multiplied_digits(10020030040050006)
print(result, '- Результат работы функции с числом "10020030040050006"')
