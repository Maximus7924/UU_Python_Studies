# Практическая задача - реформат контактов ( контакты реально мои )
# Обработка контактов из Гугла с выводом только следующих полей:
# 0, 2, 8, 22

import pandas as pd


data = './files/google_csv_contacts.csv' # контакты экспортированы в стандарте CSV-GOOGLE

# собственно контейнер со всеми данными с которым буду работать

contacts = pd.read_csv(data)

# информация о "контейнере" о всех полях и объектах

print(contacts.info())

# проверка необходимых колонок для работы с спискомw

print(contacts[['First Name', 'Last Name', 'Nickname', 'Phone 1 - Value']])

# пройтись по датафрейму и исключить любы строки содержащие "NaN" для этого применим .dropna ( расшивровка имени очевидна Drop None Available)

sorted_contacts = contacts[['First Name', 'Last Name', 'Nickname', 'Phone 1 - Value']].dropna()

# делаем новый файл с отсортированным по критерию списком, индекс=тру ради личного интереса оставил

sorted_contacts.to_csv("google_sorted.csv", index=True)

# ВАЖНО - ПОСЛЕ ОЦЕНКИ ЗАДАНИЯ ИСХОДНЫЕ ДАННЫЕ ИЗ ПУБЛИЧНОГО ДОСТУПА НА ГИТХАБЕ УДАЛЮ.