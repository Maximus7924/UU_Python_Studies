from math import inf

def divide(first, second):
	# ans = 0 # в принципе то и не нужно тут объявлять переменную она создаётся и сразу получает вычисляемое значение
	if second != 0:
		ans = first / second
	else:
		return inf
	return ans
