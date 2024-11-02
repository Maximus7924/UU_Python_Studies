import time
from multiprocessing import Pool

def read_info(name):
    """функция чтения строк из файла"""
    all_data = []  # локальный список функции находится только в памяти
    with open(name, 'r+') as file:
        while file.readline() != '': # пока возможно, будет добавлять в список прочтённую из файла строку
            all_data.append(file.readline())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# start_measure_s = time.time()
#
# for name in filenames:
#     read_info(name)
#
# stop_measure_s = time.time()
# measured_s = stop_measure_s - start_measure_s
#
# print(f'линейное выполнение {measured_s}')


# Многопроцессный

if __name__ == '__main__':

    start_measure_m = time.time()

    with Pool(4) as p_pool:
        p_pool.map(read_info, filenames)

    stop_measure_m = time.time()
    measured_m = stop_measure_m - start_measure_m

    print(f'параллельное выполнение {measured_m}')
