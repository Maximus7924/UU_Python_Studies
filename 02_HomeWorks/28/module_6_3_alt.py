class Horse:
	'''Лошадка'''
	def __init__(self):
		self.x_distance = 0
		self.sound = 'Frrr'
		super().__init__()
		
	def run(self, dx):
		self.x_distance += dx
	

class Eagle:
	'''Птичка'''
	def __init__(self):
		self.y_distance = 0
		self.sound = 'I train, eat, sleep, and repeat'
	
	
	def fly(self, dy):
		self.y_distance += dy
	

class Pegasus(Horse, Eagle):
	'''Мутант'''
	
	def __init__(self):
		super().__init__()

	def move(self, dx, dy):
		self.run(dx)
		self.fly(dy)
	
	def get_pos(self):
		return (self.x_distance, self.y_distance)
	
	def voice(self):
		print(self.sound)

# h1 = Horse()
# e1 = Eagle()
p1 = Pegasus()



print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
# print(e1.sound)
p1.voice()
print(Pegasus.mro())
