from math import inf

def divide(first, second):
	ans = 0
	if second != 0:
		ans = first / second
	else:
		ans = inf
	return ans
