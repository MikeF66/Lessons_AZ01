import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения:
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению:
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=20, edgecolor='black')
plt.title('Гистограмма N распределения 1000 случайных чисел')
plt.xlabel('Числа')
plt.ylabel('Частота')

plt.show()

