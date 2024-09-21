class Horse:
	'''Лошадка'''
	x_distance = 0
	sound = 'Frrr'
	
	def __init__(self):
		self.x_distance
		self.sound
		
	def run(self, dx):
		self.dx = dx
		run_ = self.x_distance + self.dx
		self.x_distance = run_
		return run_
	

class Eagle:
	'''Птичка'''
	y_distance = 0
	sound = 'I train, eat, sleep, and repeat'
	
	def __init__(self):
		self.y_distance
		self.sound
	
	
	def fly(self, dy):
		self.dy = dy
		fly_ = self.y_distance + self.dy
		self.y_distance = fly_
		return fly_
	

class Pegasus(Horse, Eagle):
	'''Мутант'''
	
	def __init__(self):
		self.x_distance = super().x_distance
		self.y_distance = super().y_distance
		self.sound = super().sound

	def move(self, dx, dy):
		self.dx = super().run(dx)
		self.dy = super().fly(dy)
	
	def get_pos(self):
		return (self.x_distance, self.y_distance)
	
	def voice(self):
		self.sound = super().sound
		print(self.sound)
	
h1 = Horse()
e1 = Eagle()
p1 = Pegasus()

# h1.run(10)
# print(h1.x_distance)
# h1.run(20)
# print(h1.x_distance)

# e1.fly(5)
# print(e1.y_distance)
# e1.fly(45)
# print(e1.y_distance)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
# print(Pegasus.mro())
