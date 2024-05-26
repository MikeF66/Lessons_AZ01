import numpy as np
import matplotlib.pyplot as plt

# data_set_1 :
x1 = np.random.rand(5)  # массив из 5 случайных чисел
y1 = np.random.rand(5)
print('data_set_1:')
print(x1)
print(y1)
print('')

data_set_2 = np.random.rand(10, 2)  # массив из 10x2 случайных чисел
x2 =  data_set_2[:,0]
y2 =  data_set_2[:,1]
print('data_set_2:')
print(x2)
print(y2)

# Создание фигуры (canvas) и двух подграфиков ax1 и ax2 на ней
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) # 1 строка, 2 столбца, размеры листа 10х5 дюймов

ax1.scatter(x1, y1, color='blue')  # диаграмма рассеяния для data_set_1
ax1.set_title('Диаграмма рассеяния data_set_1')
ax1.set_xlabel('Координата X1')
ax1.set_ylabel('Координата Y1')

ax2.scatter(x2, y2, color='red')  # диаграмма рассеяния для data_set_2
ax2.set_title('Диаграмма рассеяния data_set_2')
ax2.set_xlabel('Координата X2')
ax2.set_ylabel('Координата Y1')

plt.show()

