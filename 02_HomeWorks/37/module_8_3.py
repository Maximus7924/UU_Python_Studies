class Car:
    """ Главный класс объектов типа автомобиль """
    def __init__(self, model, __vin, __numbers):
        self.model = model # модель авто
        self.vin = __vin # вин автомобиля
        self.numbers = __numbers # номер автомобиля
        self.__is_valid_vin() # вызов метода при создании объекта
        self.__is_valid_numbers() # вызов метода при создании объекта

        
    def __is_valid_vin(self):
        """ проверка на корректность ВИНа автомобиля """
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        # если передано не целое число. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
    # Возвращает True, если исключения не были выброшены.
        
        if isinstance(self.vin, int) != True:
            raise IncorrectVinNumber('Некорректный тип VIN номера.')
        
        if self.vin < 1000000 or self.vin > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для VIN номера.')
            
    
    def __is_valid_numbers(self):
        """ проверка на корректность НОМЕРа автомобиля """
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        # если передана не строка. (тип данных можно проверить функцией isinstance).
    # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        # переданная строка должна состоять ровно из 6 символов.
    # Возвращает True, если исключения не были выброшены.
        if isinstance(self.numbers, str) != True:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров.')
        
        if len(self.numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера.')
    

class IncorrectVinNumber(Exception):
    """Исключение если ВИН не прошёл проверку на корректность"""
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    """Исключение если НОМЕР не прошёл проверку на корректность"""
    def __init__(self, message):
        self.message = message


# Данные для проверки

# try:
#   first = Car('Model1', 1000000, 'f123dj')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{first.model} успешно создан')
#
# try:
#   second = Car('Model2', 3010, 'т001тр')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{second.model} успешно создан')
#
# try:
#   third = Car('Model3', 2020202, 'нет номера')
# except IncorrectVinNumber as exc:
#   print(exc.message)
# except IncorrectCarNumbers as exc:
#   print(exc.message)
# else:
#   print(f'{third.model} успешно создан')

# Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера
