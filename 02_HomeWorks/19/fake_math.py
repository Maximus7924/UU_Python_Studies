def divide(first, second):
	# ans = 0 # в принципе то и не нужно тут объявлять переменную она создаётся и сразу получает вычисляемое значение
	if second == 0:
		return 'Ошибка'
	else:
		ans = first / second
	return ans

# print(divide(4, 0))