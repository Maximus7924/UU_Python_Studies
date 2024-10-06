# Переменные по заданию

team1_num = int(5)
team2_num = int(6)
score_1 = int(40)
score_2 = int(42)
team1_time = float(1552.512)
team2_time = float(2153.31451)
tasks_total = score_1 + score_2
time_avg = float((team1_time + team2_time)/tasks_total)

team1_name = str('Мастера кода')
team2_name = str('Волшебники данных')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team2_time > team1_time:
        return f'Победа команды {team1_name}'
    elif score_1 < score_2 or score_1 == score_2 and team2_time < team1_time:
        return f'Победа команды {team2_name}'
    else:
        return f'Ничья'

# Использование метода "%"

print("В команде %s участников: %s !" % (team1_name, team1_num))
print("Итого сегодня в командах участников: %s и %s !" % ( team1_num, team2_num))

# Использование метода ".format"

print("Команда {} решила задач: {}!".format(team2_name, score_2))
print("{} решили задачи за {} c !".format(team2_name, team1_time))

# Использование метода "f'..{}.."

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()} !')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')


# в действительности расчёт time_avg может немного отличаться от цифр по заданию так как методика расчёта среднего
# несколько будет отличаться, типа (время_команды/кол-во_задач_команды) и это для каждой команды сложить и поделить
# на общее кол-во команд, .... так, несущественно....

