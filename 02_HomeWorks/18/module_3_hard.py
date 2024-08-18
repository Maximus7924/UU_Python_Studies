
def calculate_structure_sum(*data_structure):
	ds = data_structure
	
	def summ(ds):
		result = 0
		if isinstance(ds, int):
			result += ds
		elif isinstance(ds, str):
			result += len(ds)
		elif isinstance(ds, list):
			for element in ds:
				result += summ(element)
		elif isinstance(ds, tuple):
			for element in ds:
				result += summ(element)
		elif isinstance(ds, dict):
			for key, value in ds.items():
				result += summ(key) + summ(value)
		return result
	result = summ(ds)
	return result


print(calculate_structure_sum([
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]))