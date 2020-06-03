import matplotlib.pyplot as plt
import numpy as np

from source.formulas import pow_2

print("Enter x:")
variable_name = input()
print(variable_name)

# Задаем зависимоти
x = np.linspace(0, 0.1, 50)  # Массив из (p3) значений на отрезке (p1;p2)

y1 = x          # Функция от заданных значений х
y2 = pow_2(x)   # Вторая функция, заданная с использованием формулы, определенной в файле formulas

# Построение графика
plt.title("Зависимости")  # Заголовок
plt.xlabel("x")           # Ось абсцисс (x)
plt.ylabel("y1, y2")      # Ось ординат (y)
plt.grid()                # Включение отображения сетки

plt.plot(x, y1, x, y2)    # Построение графика (теперь он существует где-то в памяти)
plt.show()                # Вывод графика на экран
