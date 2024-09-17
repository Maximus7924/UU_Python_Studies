
class Vehicle:
	'''общий Класс для автомобилей'''
	__COLOR_VARIANTS = ['красный', 'синий', 'серый']
	
	def __init__(self, owner, __model, __engine_power, __color):
		self.owner = owner
		self.__model = __model
		self.__engine_power = __engine_power
		self.__color = __color
	
	def get_model(self):
		return f' Модель: {self.__model}'
	
	def get_horsepower(self):
		return f' Мощность двигателя: {self.__engine_power}'
	
	def get_color(self):
		return f' Цвет: {self.__color}'
	
	def print_info(self):
		print(Vehicle.get_model(self),
		      Vehicle.get_horsepower(self),
		      Vehicle.get_color(self),
		      f'Владелец: {self.owner}')
	
	def set_color(self, new_color):
		colors = Vehicle.__COLOR_VARIANTS
		new_color = new_color.casefold()
		for i in colors:
			if new_color != i:
				continue
			elif new_color == i:
				self.__color = new_color
				print(f'Мы сменили цвет на {new_color}')
				return
		print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
	'''конкретно для типа Седан'''
	__PASSENGERS_LIMIT = 5
	
	pass




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'синий')

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('СерыЙ')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()