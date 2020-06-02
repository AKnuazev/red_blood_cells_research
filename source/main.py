import matplotlib.pyplot as plt
import numpy as np

print("Enter x:")
variable_name = input()
print(variable_name)

# Линейная зависимость
x = np.linspace(0, 0.1, 50)  # Массив из p3 значений на отрезке (p1;p2)
y1 = x ** 2  # Функция от них
y2 = x
print(x)

# Построение графика
plt.title("Зависимости") # заголовок
plt.xlabel("x")          # ось абсцисс (x)
plt.ylabel("y1, y2")     # ось ординат (y)
plt.grid()               # включение отображение сетки
plt.plot(x, y1, x, y2)   # построение графика
plt.show()               # вывод графика на экран
