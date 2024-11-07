import inspect


def introspection_info(obj):
    for name, value in inspect.getmembers(obj):
        if name == '__class__':
            print(f'Класс объекта {value}')
        else:
            continue
    print('Обнаруженные атрибуты')
    for name, value in inspect.getmembers(obj):  # Атрибуты
        if name.startswith('__'):
            continue
        else:
            print(f'\t{name} : {value}')
    print('Если обнаружены методы ниже список')
    for name, value in inspect.getmembers(obj):  # Методы
        if inspect.ismethod(value):
            print(f'\t"{name}" это метод:\n\t\t {value}')
        else:
            continue
    print(f'Модуль из которого запущено:')
    for name, value in inspect.getmembers(obj):  # Модуль
        if name == '__module__':
            print(f'\t{value}')
        else:
            continue


class Circle:
    """круг наследуется от ФИГУРЫ и дополнительно имеет аттрибуты : площадь и длина окружности"""
    
    def __init__(self, size=0):
        self.size = size
        self.length = 2 * 3.1415 * self.size
        self.area = 3.1415 * self.size ** 2


class Triangle:
    """треугольник по-умолчанию равносторонний и вписан в окружность радиусом size"""
    
    def __init__(self, size=0):
        self.size = size
        # флаг определяющий треугольник вписан или описан ( по-умолчанию вписан )
        self.flag = False
        # периметр вписанного в окружность треугольника
        self.length = 3 * self.size * (3 ** 1 / 2)
        # площадь вписанного в окуржность треугольника
        self.area = ((self.size * (3 ** 1 / 2)) ** 2 * (3 ** 1 / 2)) / 4
    
    def outer2inner(self, flag: bool):
        # атрибут FLAG в методе меняет параметры расчитываемого треугольника
        self.flag = flag
        if self.flag == False:
            self.length = 3 * self.size * (3 ** 1 / 2)
            self.area = ((self.size * (3 ** 1 / 2)) ** 2 * (3 ** 1 / 2)) / 4
        else:
            self.length = 3 * self.size * 2 * (3 ** 1 / 2)
            self.area = ((self.size * 2 * (3 ** 1 / 2)) ** 2 * (3 ** 1 / 2)) / 4


c1 = Circle(9)
t1 = Triangle(c1.size)

introspection_info(c1)
introspection_info(t1)


# после многоразового запуска\отладки появилось понимание необходимости грамотного оформления док-стрингов для всего:)