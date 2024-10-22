from time import sleep
from datetime import datetime
from threading import Thread


def write_words_linear(*args):
    """функция декорирования для последовательного (линейного) выполнения программы"""
    argdict = {} # словарь будет содержать имя файла как ключ и кол-во строк записи в него как значение
    for c in range(len(args)):
        argdict.update({f'l_example{c + 1}.txt': f'{args[c]}'})
    
    def linear_counter(write_function):
        #начинаем отсчёт времени выполнения
        time_start = datetime.now()
        # извлекаем из словаря "пары" и меняем местами для подстановки в функцию как аргументы (задание определило порядок и значение аргументов)
        for filename, word_count in argdict.items():
            write_function(int(word_count), filename)
        # функция перебрала и выполнила все пары в словаре, можно останавливать секундомер
        time_stop = datetime.now()
        time_elaps = time_stop - time_start
        print(f'Выполнение записи в файлы ЛИНЕЙНО-ПОСЛЕДОВАТЕЛЬНО заняло {time_elaps}')
    
    return linear_counter


def write_words_threaded(*args):
    """функция декорирования для параллельного (поточного) выполнения программы"""
    argdict = {} # словарь будет содержать имя файла как ключ и кол-во строк записи в него как значение
    for c in range(len(args)):
        argdict.update({f't_example{c + 1}.txt': f'{args[c]}'})
    
    def threaded_counter(write_function):
        # начинаем отсчёт времени выполнения
        time_start = datetime.now()
        threads = [] # в этом списке будут "ссылки" на созданные ниженаписаным циклом потоки
        for filename, word_count in argdict.items():
            thread_name = filename[:-4] # даём имя потоку в конструкторе по названию файла (без суффикса .тхт)
            thread = Thread(target=write_function, name=thread_name, args=(int(word_count), filename))
            threads.append(thread) # добавляем ссылку на поток в лист и так проитерируется для всех пар словаря
            thread.start() # сразу стартуем поток с сформированными значениями
        
        [thread.join() for thread in threads] # такая "сборка" джойнит все созданные потоки что-бы "главный" поток дождался выполнения всех
        time_stop = datetime.now()
        time_elaps = time_stop - time_start
        
        print(f'Выполнение записи в файлы ПОТОЧНО-ПАРАЛЛЕЛЬНО заняло{time_elaps}')
    return threaded_counter


@write_words_linear(10,30,200,100)
def write_words(word_count, filename):
    """Функция ведёт запись слов "Какое-то слово № <номер слова по порядку>"
    в соответствующий файл с прерыванием после записи каждого на 0.1 секунду
    word_count - количество записываемых слов
    filename - имя файла для записи"""
    with open(filename, "w", encoding="utf-8") as file:
        w_counter = 1
        while w_counter <= word_count:
            file.write(f'Какое-то слово № {w_counter}\n')
            w_counter += 1
            sleep(0.1)
            
    print(f'Завершилась запись в файл {filename}')


@write_words_threaded(10, 30, 200, 100)
def write_words(word_count, filename):
    """Функция ведёт запись слов "Какое-то слово № <номер слова по порядку>"
    в соответствующий файл с прерыванием после записи каждого на 0.1 секунду
    word_count - количество записываемых слов
    filename - имя файла для записи"""
    with open(filename, "w", encoding="utf-8") as file:
        w_counter = 1
        while w_counter <= word_count:
            file.write(f'Какое-то слово № {w_counter}\n')
            w_counter += 1
            sleep(0.1)
    
    print(f'Завершилась запись в файл {filename}')
