my_string = input("Введите любой текст : ")
print(my_string, ", эта строка содержит ", len(my_string), "символов.\n")
print("Заглавными :\n", my_string.upper())
print("Прописными :\n", my_string.lower())
print("Без пробелов :\n", my_string.replace(' ', '')) # pycharm автодополнением даёт конструкцию с ошибкой, странно.
print("Первый символ строки :\n", my_string[0])
print("Последний символ строки :\n", my_string[-1])
