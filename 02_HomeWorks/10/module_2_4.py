# альтернативное решение подозреваю

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = []
for i in numbers:
    for j in numbers:
        if j % i == 0:
            if j > i != 1:
                not_primes.append(j)

numbers_set = set(numbers)
not_primes_set = set(not_primes)
primes_set = set.difference(numbers_set, not_primes_set)
primes_set.discard(1)

print('Исходный список чисел :', numbers_set)
print('Список простых чисел :', primes_set)
print('Список непростых чисел', not_primes_set)
