immutable_var = ("One", 2, 3.0)
print(immutable_var)
print(type(immutable_var))
print(type(immutable_var[0]), type(immutable_var[1]), type(immutable_var[2]))
# попытка изменить строковый элемент на целочисленный
try:
    immutable_var[0] = 1
except:
    print("Изменение кортежей недопустимо")
# собственно тип "кортеж" и был задуман с отсутсвием возможности изменений
mutable_list = (["One", 2, 3.0])
print(mutable_list)
print(type(mutable_list))
print(type(mutable_list[0]), type(mutable_list[1]), type(mutable_list[2]))
try:
    mutable_list[0] = 1
    mutable_list[1] = "Two"
    print(mutable_list)
    print(type(mutable_list[0]), type(mutable_list[1]), type(mutable_list[2]))
except:
    print("Изменение списка невозможно")
else:
    print("Значения списка изменились успешно")