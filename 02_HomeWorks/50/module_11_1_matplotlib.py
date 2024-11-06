import numpy as np
import matplotlib.pyplot as plt

# ИНТЕРЕСНАЯ СИММЕТРИЯ В "МАГИЧЕСКОМ" КВАДРАТЕ

# Объявление "магического" квадрата
mgsqr = np.array([[4,14,15,1],[9,7,6,12],[5,11,10,8],[16,2,3,13]])

# массивы с координатами для построения чертежа
x_axis=[]
y_axis=[]

# вычисление координат точки по значению числа в сетке
for point in range(1,17):
    point = np.where(mgsqr == point)
    x_axis.append(point[1].item())
    y_axis.append(point[0].item())

# проверочный вывод значений массивов координат
# print(x_axis)
# print(y_axis)

# рисование фигуры "последовательного пути" чисел в магическом квадрате
fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
plt.show()