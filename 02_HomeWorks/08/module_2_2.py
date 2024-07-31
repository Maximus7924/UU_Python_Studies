# переменные first, second, third завернул в целочисленные по условиям задачи.
first =  int(input('Введите первое целое число :\n'))
print(first)
second = int(input('Введите второе целое число :\n'))
print(second)
third = int(input('Введите третье целое число :\n'))
print(third)

if first == second and first == third:
    print('Все введённе числа совпадают, код 3')
elif first == second or first == third or second == third:
    print('Только два из введённых чисел совпадают, код 2')
else:
    print('Всее числа разные, код 0')