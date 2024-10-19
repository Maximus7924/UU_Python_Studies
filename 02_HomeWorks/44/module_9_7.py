def is_prime(func):
    """функция дополняющая вывод проверкой на "простоту" результата другой функции"""
    def solver(*args):
        """функция проверки на "простоту" числа"""
        number = func(*args)
        for i in range(2, number+1):
            if (number % i) == 0 and i != number:
                print('Составное')
                break
            elif (number % i) == 0:
                print('Простое')
                break
        return number
    return solver


@is_prime
def sum_three(*args):
    resultat = 0
    for i in [*args]:
        resultat += i
    return resultat


# Пример:
result = sum_three(2, 3, 6)
print(result)
result = sum_three(7, 1, 10)
print(result)
result = sum_three(100, 10, 7)
print(result)
result = sum_three(1, 2, 4)
print(result)
#
# Результат консоли:
# Простое
# 11