def apply_all_func(int_list, *functions):
    # """Вызывает каждую функцию к переданному списку int_list и возвращает словарь,
    # где ключом будет название вызванной функции, а значением - её результат работы со списком int_list."""
    res_dict = {}
    for function in functions:
        res_dict.update({function.__name__ : function(int_list)})
    return res_dict

# Код для проверки

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
# Вывод на консоль:
# {'max': 20, 'min': 6}
# {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
