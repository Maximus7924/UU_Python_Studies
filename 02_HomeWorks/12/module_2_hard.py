cipher_1 = int(input("Введите первое поле пароля : "))

cipher_1_divlist = []
cipher_1_divlistsumm = []

for c1l in range(1, cipher_1 + 1):
    if cipher_1 % c1l == 0:
        cipher_1_divlist.append(c1l)

cipher_1_divlist.remove(1)

print('Кратные числа : ', cipher_1_divlist)

for c1ls in cipher_1_divlist:
    c1 = 1
    while c1 <= c1ls/2:
        c2 = c1ls - c1
        c3 = str(f"{c1} и {c2}")
        if c1 == c2:
            break
        else:
            cipher_1_divlistsumm.append(c3)
        c1 += 1
print('Пары слогаемых для кратных чисел : ', cipher_1_divlistsumm)
