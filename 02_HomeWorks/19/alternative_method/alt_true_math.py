from math import inf

def divide(first, second):
	try:
		ans = first / second
	except ZeroDivisionError:
		return inf
	else:
		return ans
