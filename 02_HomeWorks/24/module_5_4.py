class House:
	
	houses_history = []
	
	def __new__(cls, *args, **kwargs):
		cls.houses_history.append(args[0])
		return object.__new__(cls)
	
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
	
	def __del__(self):
		print(f'{self.name} снесён, но он останется в истории')
		return self


h1 = House('Kalinina', 12)
print(House.houses_history)
h2 = House('Svetlanskaya', 25)
print(House.houses_history)
h3 = House('Lenina', 9)
print(House.houses_history)

# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)