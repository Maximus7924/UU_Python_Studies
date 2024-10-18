def all_variants(text):

    stroka = text
    cycle_counter = 1
    while cycle_counter <= len(stroka):
        for s in range(len(stroka)):
            if len(stroka[s:s+cycle_counter]) < cycle_counter:
                pass
            else:
                yield (stroka[s:s + cycle_counter])
        cycle_counter +=1

b = all_variants('abcd')
for i in b:
    print(i)


# Пример работы функции:
#
    # a = all_variants("abc")
    # for i in a:
    #     print(i)
# Вывод на консоль:
#     a
#     b
#     c
#     ab
#     bc
#     abc
