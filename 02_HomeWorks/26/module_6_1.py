
class Animal:
	'''Животные могут быть как хищники так и млекопитающие'''
	def __init__(self, name, alive=True, fed=False):
		self.name = name
		self.alive = alive
		self.fed = fed
		
	def eat(self, food):
		self.food = food
		if food.edible == True:
			print(f'{self.name} съел {food.name}')
			self.fed = True
		else:
			print(f'{self.name} не стал есть {food.name}')
			self.alive = False
			self.fed = None # если не живое то не имеет смысла накормленность, от себя вставил

class Plant:
	'''Растения могут быть съедобные и ядовитые'''
	def __init__(self, name, edible=False):
		self.name = name
		self.edible = edible
		if isinstance(self, Fruit):
			self.edible = True

class Mammal(Animal):
	'''Млекопитающие кушают растения'''
	def name(self, name):
		self.name = name
	
class Predator(Animal):
	'''Хищники обычно кушают млекопитающих'''
	def name(self, name):
		self.name = name
	
class Flower(Plant):
	'''Цветы могут быть невкусными или ядовитыми'''
	def name(self, name):
		self.name = name

class Fruit(Plant):
	'''Фрукты обычно съедобные'''
	def name(self, name):
		self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

a3 = Predator('Злой питон')
print(a3.name, a3.alive, a3.fed)
a3.eat(p2)
print(a3.alive, a3.fed)
a3.eat(p1)
print(a3.alive, a3.fed)
