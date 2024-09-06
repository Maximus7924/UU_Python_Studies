from mpmath import hyp2f0


class House:
	def __init__(self, name, number_of_floors):
		self.name = name
		self.number_of_floors = number_of_floors
	
	def go_to(self, new_floor):
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
		return self.number_of_floors
	
	def __str__(self):
		return (f'Название : {self.name}, кол-во этажей : {self.number_of_floors}')


h1 = House('Kalinina', 12)
h2 = House('Svetlanskaya', 25)

# print(h1.name, h1.number_of_floors)
# # h1.go_to(8)
# # h1.go_to(13)

print(h1)
print(len(h1))

print(h2)
print(len(h2))
