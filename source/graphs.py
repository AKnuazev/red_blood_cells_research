import matplotlib.pyplot as plt    # Импортируем библеотеку для работы с графиками
import numpy as np                 # Импортируем библеотеку для работы с массивами

from source.formulas import pow_2, first_difr_min, strange_func_of_Imin  # Импортируем необходимые нам формулы из файла formulas

# Задаем зависимоти
x = np.linspace(0, 0.5, 1000)  # Массив из (p3) значений на отрезке (p1;p2)

# константы:
q = 39.7
N = 1000
e1 = 0.03
e2 = 0.1
e3 = 0.2

y1 = strange_func_of_Imin(x, q, N, e1)
y2 = strange_func_of_Imin(x, q, N, e2)
y3 = strange_func_of_Imin(x, q, N, e3)

# Построение графика
plt.title("Зависимости")  # Заголовок
plt.xlabel("x")           # Ось абсцисс (x)
plt.ylabel("y1, y2")      # Ось ординат (y)
plt.grid()                # Включение отображения сетки

plt.plot(x, y1, x, y2, x, y3)    # Построение графика (теперь он существует где-то в памяти)

# Подписи на графике
plt.legend(['При e=0.03', 'При e=0.1', 'При e=0.2'])

plt.show()                # Вывод графика на экран
