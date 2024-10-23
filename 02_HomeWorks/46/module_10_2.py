from threading import Thread
from time import sleep

class Knight(Thread):
    
    def __init__(self, name:str, power:int):
        super().__init__()
        self.name = name # имя рыцаря
        self.power = power # сила рыцаря (показатель скорости уничтожения врагов)
        self.enemy = 100 # количество напавших врагов
        
    
    def run(self):
        print(f'{self.name}, на нас напали!')
        # битва
        enemy = self.enemy
        days = 0
        while enemy > 0:
            enemy -= self.power
            days += 1
            sleep(1.0)
            print(f'{self.name}, сражается {days} день(дня)..., осталось {enemy} воинов.')
        # битва завершилась
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')
    
    
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

