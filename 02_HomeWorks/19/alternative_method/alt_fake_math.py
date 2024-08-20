def divide(first, second):
	try:
		ans = first / second
	except ZeroDivisionError:
		return 'Ошибка'
	else:
		return ans
