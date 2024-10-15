# 01 - Лямбда функция

first = 'Мама мыла раму'
second = 'Рамена мало было'

result_1 = list(map(lambda f,s: f == s, first, second))
print(result_1)

# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
########################################################################################################################
# 02 - Замыкание

def get_advanced_writer(file_name):
    file = open(file_name, "a+", encoding="utf-8")
    file.close()


    def write_everything(*data_set):
        with open(file_name, "a+", encoding="utf-8") as file:
            for l in data_set:
                line = f'{str(l)}\n'
                file.write(line)
    
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Запишет данные в файл в таком виде: картинка.... записывает и дозаписывает, проверял самолично.
########################################################################################################################
# 03 - Метод __call__:

from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words
        
        
    def __call__(self):
        word = choice(self.words)
        return word
        

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
########################################################################################################################