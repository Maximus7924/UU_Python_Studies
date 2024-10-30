from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    """Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и
guest - гость, который сидит за этим столом (по умолчанию None)"""
    def __init__(self, number, guest = None):
        self.number = number # номер стола
        self.guest = guest # гость сидящий за столом ( по факту поток )


class Guest(Thread):
    """Должен наследоваться от класса Thread (быть потоком).
Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
Обладать атрибутом name - имя гостя.
Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд."""
    def __init__(self, name):
        super().__init__() # наследование инита с методами от "супера" который база для потоков
        self.name = name  # имя гостя
    
    def run(self):
        wait = randint(1, 2) # генерация случайности в диапазоне
        sleep(float(wait)) # засыпание на случайное время
        
        
class Cafe:
    """Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей)."""
    def __init__(self, *tables):
        self.tables = tables # список столов в заведении
        self.wait = Queue() # очередь посетителей
        
        
    def guest_arrival(self, *guests):
        """Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди"."""
        # self.guests = guests
  
        table_counter = 0
        
        for guest in guests:
            if table_counter <= (len(self.tables) - 1) and tables[table_counter].guest is None:
                tables[table_counter].guest = guest
                tables[table_counter].guest.start()
                tables[table_counter].guest.join()
                print(f'{tables[table_counter].guest.name} сел(-а) за стол номер {tables[table_counter].number}')
                table_counter += 1
            else:
                self.wait.put(guest)
                print(f'{guest.name} в очереди')

    
    def discuss_guests(self):
        """Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)"""
        
        try:
            while not self.wait.empty(): # цикл проверки очереди пока она не пуста ------
                for table in self.tables: # обход состояния столов в кафе
                    if table.guest is not None and not table.guest.is_alive(): # если гость за столом и процесс умер
                        print(f'{table.guest.name} за текущим столом {table.number} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None # удаление гостя из за стола
                    elif table.guest is None: # если за столом нет гостя, т.е. стол пустует
                        table.guest = self.wait.get() # достаём следующего из очереди
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
                        table.guest.join()
        finally:
            for table in self.tables:
                if table.guest is None:
                    pass
                elif table.guest is not None and table.guest.is_alive():
                    while table.guest.is_alive():
                        sleep(3.0)
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} за текущим столом {table.number} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None  # удаление гостя из за стола


# ПРИМЕР ВЫПОЛНЕНИЯ ПРОГРАММЫ

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()