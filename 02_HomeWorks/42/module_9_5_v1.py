class Iterator:
    def __init__(self, start, stop, step=1):
        """Метод принимает значения начала и конца итерации, а также шага.
        В этом методе в первую очередь проверяется step на равенство 0.
        Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')"""
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError
        self.pointer = self.start
        

    
    def __iter__(self):
        """Метод сбрасывающий значение pointer на start и возвращающий сам объект итератора."""
        self.pointer = self.start
        return self

    
    def __next__(self):
        """Метод увеличивающий атрибут pointer на step.
        В зависимости от знака атрибута step итерация завершиться либо когда pointer станет больше stop, либо меньше stop.
        Учтите это при описании метода."""
        self.pointer += self.step
        
        if self.step > 0 and self.pointer < self.stop:
            return self.pointer
        
        if self.step < 0 and self.pointer > self.stop:
            return self.pointer
        
        if self.pointer == self.stop:
            return self.pointer
        
        if self.pointer > self.stop:
            pass
        raise StopIteration

    
class StepValueError(ValueError):
    pass


# Пример выполняемого кода:

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
#
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
#
#
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1

