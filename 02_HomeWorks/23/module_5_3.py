
class House:
	def __init__(self, name, number_of_floors):
		'''Основной метод с именем здания и кол-вом этажей'''
		self.name = name
		self.number_of_floors = number_of_floors
	
	def go_to(self, new_floor):
		'''Метод передвижения на другой этаж'''
		self.new_floor = new_floor
		
		print(f'Попытка уехать на этаж {self.new_floor}')
		if new_floor > self.number_of_floors or new_floor < 1:
			print('Такого этажа не существует')
		else:
			floor = 1
			while floor <= new_floor:
				print(floor)
				floor += 1
			print(f'Поездка на {self.new_floor} этаж успешна')
	
	def __len__(self):
		'''Метод вывода количества этажей'''
		return self.number_of_floors
	
	def __str__(self):
		'''Метод вывода названия здания и кол-ва этажей'''
		return f'Название : {self.name}, кол-во этажей : {self.number_of_floors}'
	
	def __eq__(self, other):
		'''булевый Метод сравнения кол-ва этажей у зданий '''
		return self.number_of_floors == other.number_of_floors
	
	def __lt__(self, other):
		'''Метод "меньше чем..."'''
		return self.number_of_floors < other.number_of_floors
	
	def __le__(self, other):
		'''Метод "меньше или равен..."'''
		return self.number_of_floors <= other.number_of_floors
	
	def __gt__(self, other):
		'''Метод "больше чем..."'''
		return self.number_of_floors > other.number_of_floors
	
	def __ge__(self, other):
		'''Метод "больше или равен..."'''
		return self.number_of_floors >= other.number_of_floors
	
	def __ne__(self, other):
		'''Метод "не равно..."'''
		return self.number_of_floors != other.number_of_floors
	
	def __add__(self, other):
		'''Метод увеличивающй кол-во этажей, новое значение это "other"'''
		self.number_of_floors = self.number_of_floors + other
		return self
	
	def __radd__(self, other):
		'''Метод сложения объектов'''
		self.number_of_floors = other + self.number_of_floors
		return self
	
	def __iadd__(self, other):
		'''Метод "приращения" типа +=...'''
		self.number_of_floors += other
		return self


h1 = House('Kalinina', 12)
h2 = House('Svetlanskaya', 25)

print(h1)
print(len(h1))
print(h2)
print(len(h2))

print(h1 == h2) # __eq__
h1 = h1 + 13 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

