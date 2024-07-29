print('Словарь\n')
my_dict = {'Юля': 1977, 'Максим': 1979, 'Даша': 2005, 'Настя': 2011}
print(my_dict)
print(my_dict.get('Юля'))
print(my_dict.pop('Бабушка', 'нет данных'))
my_dict.update({'Мама': 1959, 'Папа': 1961, })
print(my_dict)
father = my_dict.pop('Папа')
print(father)
print(my_dict)

print('\nМножества\n')
my_set = {1, 9, 7, 7, 1, 9, 7, 9, 'Мама'}
print(my_set)
my_set_add = {6, 8}
my_set.update(my_set_add)
print(my_set)
my_set.remove('Мама')
print(my_set)
