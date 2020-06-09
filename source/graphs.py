import matplotlib.pyplot as plt  # Импортируем библеотеку для работы с графиками
import numpy as np  # Импортируем библеотеку для работы с массивами

from source.formulas import pow_2, first_difr_min, \
    strange_func_of_Imin  # Импортируем необходимые нам формулы из файла formulas

from random import randint

# Задаем зависимоти
x = np.linspace(0, 0.5, 1000)  # Массив из (p3) значений на отрезке (p1;p2)

# константы:
q = 39.7
N = 1000
e1 = 0.03
e2 = 0.1
e3 = 0.2


# y1 = strange_func_of_Imin(x, q, N, e1)
# # y2 = strange_func_of_Imin(x, q, N, e2)
# # y3 = strange_func_of_Imin(x, q, N, e3)
#
# # Построение графика
# plt.title("Зависимости")  # Заголовок
# plt.xlabel("x")  # Ось абсцисс (x)
# plt.ylabel("y1, y2")  # Ось ординат (y)
# plt.grid()  # Включение отображения сетки
#
# plt.plot(x, y1)  # Построение графика (теперь он существует где-то в памяти)
#
# # Подписи на графике
# plt.legend(['При e=0.03', 'При e=0.1', 'При e=0.2'])


# plt.show()                # Вывод графика на экран

class particle:
    def __init__(self, radius=0):
        self.radius = radius


def make_dists(N):
    M = 100

    # Равномерное
    types_ravn = np.zeros(M)

    for i in range(N):
        type_number = randint(0, M - 1)
        types_ravn[type_number] += 1

    x_ravn = np.linspace(0, M, M)
    y_ravn = types_ravn

    # Нормальное
    particles_norm = np.random.normal(M/2, M / 2, size=N)
    types_norm = np.zeros(M)

    for type in particles_norm:
        if int(type) < 100 and int(type) > 0:
            types_norm[int(type)] += 1

    x_norm = len(types_norm)
    y_norm = types_norm

    # Построение графика
    fig, axes = plt.subplots(2, 1)

    axes[0].bar(x_ravn, y_ravn)
    axes[1].bar(x_ravn, y_norm)

    plt.show()

def make_ravn_dists(N):
    M = 100

    # Равномерное
    types_ravn = np.zeros(M)

    for i in range(N):
        type_number = randint(0, M - 1)
        types_ravn[type_number] += 1

    x = np.linspace(0, M, M)
    y = types_ravn

    # Построение графика
    fig, ax = plt.subplots()

    ax.bar(x, y)

    plt.show()

# def make_normal_dist(N):
#     M = 100
#
#     particles = np.random.normal(M / 2, M / 2, size=N)
#     types = np.zeros(M)
#
#     for type in particles:
#         types[int(type)] += 1
#
#     x = np.linspace(0, M, M)
#     y = types
#
#     # Построение графика
#     fig, ax = plt.subplots()
#
#     ax.bar(x, y)
#
#     ax.set_facecolor('seashell')
#     fig.set_facecolor('floralwhite')
#
#     plt.show()
