# 1. Функция с параметрами по умолчанию :

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('\n Функции с параметрами по умолчанию. \n')
print_params(2, 'string', False) # сработало
print_params(67, 'things') # сработало
print_params(b = 25) # сработало, т.к. явно переопределили одним знаком =
print_params(c = [1,2,3]) # сработало, т.к. явно переопределили одним знаком =
print_params() # сработало с значениями по умолчанию

# 2. Распаковка параметров :
values_list = [1979, 'YearOfBirth', True]
values_dict = {
    'a': 2005,
    'b': 'DariaBirth',
    'c': True
}

print('\n Распаковка параметров. \n')
print_params(*values_list) # сработало как и должно
print_params(**values_dict) # сработало как и должно

print('\n Распаковка + отдельные параметры: \n')
values_list_2 = [2011, 'NastyaBirth']
print_params(*values_list_2, 42) # сработало
