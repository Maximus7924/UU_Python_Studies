print('Словарь\n')
my_dict = {'Юля': 1977, 'Максим': 1979, 'Даша': 2005, 'Настя': 2011}
print('Начальный словарь :', my_dict)
print("Значение ключа 'Юля' :", my_dict.get('Юля'))
print("Поиск ключа 'Бабушка' :", my_dict.pop('Бабушка', 'нет данных'))
my_dict.update({'Мама': 1959, 'Папа': 1961, })
print('Обновлённый словарь :', my_dict)
father = my_dict.pop('Папа')
print("Значение вытащенного из словаря ключа 'Папа' :", father)
print('Итоговый слловарь :', my_dict)

print('\nМножества\n')
my_set = {1, 9, 7, 7, 1, 9, 7, 9, 'Мама'}
print('Множество :', my_set)
my_set_add = {6, 8}
my_set.update(my_set_add)
print('Обновлённое множество :', my_set)
my_set.remove('Мама')
print('Итоговое множество с удалённым элементом :', my_set)