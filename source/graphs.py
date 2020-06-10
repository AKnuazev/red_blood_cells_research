import matplotlib.pyplot as plt  # Импортируем библеотеку для работы с графиками
import numpy as np  # Импортируем библеотеку для работы с массивами

from source.constants import M, diff
from source.formulas import make_ravn_dist, make_norm_dist, \
    func_of_Imin, func_of_Imax  # Импортируем необходимые нам формулы из файла formulas

# константы:
q = 39.7
e1 = 0.03
e2 = 0.1
e3 = 0.2


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


def make_Imin_graphs(N):
    x = np.linspace(0, N, N)

    y_min1 = func_of_Imin(x, q, N, e1)
    y_min2 = func_of_Imin(x, q, N, e2)
    y_min3 = func_of_Imin(x, q, N, e3)

    y_max1 = func_of_Imax(x, q, N, e1)
    y_max2 = func_of_Imax(x, q, N, e2)
    y_max3 = func_of_Imax(x, q, N, e3)

    # Построение графика
    fig, axes = plt.subplots(3, 2)
    fig.set_facecolor('whitesmoke')
    fig.suptitle('Графики Imin и Imax', size=20)

    axes[0, 0].plot(x, y_min1, color='teal', linewidth = 3)
    axes[0, 0].set_title('Imin при e=0.03', size=12)
    axes[0, 0].legend(['Imin'])

    axes[0, 1].plot(x, y_max1, color='darkorange', linewidth = 3)
    axes[0, 1].set_title('Imax при e=0.03', size=12)
    axes[0, 1].legend(['Imax'])

    axes[1, 0].plot(x, y_min2, color='teal', linewidth = 3)
    axes[1, 0].set_title('Imin при e=0.1', size=12)
    axes[1, 0].legend(['Imin'])

    axes[1, 1].plot(x, y_max2, color='darkorange', linewidth = 3)
    axes[1, 1].set_title('Imax при e=0.1', size=12)
    axes[1, 1].legend(['Imax'])

    axes[2, 0].plot(x, y_min3, color='teal', linewidth = 3)
    axes[2, 0].set_title('Imin при e=0.2', size=12)
    axes[2, 0].legend(['Imin'])

    axes[2, 1].plot(x, y_max3, color='darkorange', linewidth = 3)
    axes[2, 1].set_title('Imax при e=0.2', size=12)
    axes[2, 1].legend(['Imax'])

    plt.show()


# Выводит на экран модуль из двух графиков с равномерным и нормальным распределениями частиц по типам
def make_dists(N):
    x = np.linspace(0, M, M)
    y_ravn = make_ravn_dist(N)               # Равномерное
    y_norm = make_norm_dist(M / 2, diff, N)  # Нормальное

    # Построение графика
    fig, axes = plt.subplots(2, 1)
    fig.set_facecolor('whitesmoke')
    fig.suptitle('Графики распределений частиц', size=25)

    axes[0].bar(x, y_ravn, color='teal')
    axes[0].set_title('Равномерное распределение', size=20)
    axes[0].legend(['Количество частиц'])

    axes[1].bar(x, y_norm, color='darkorange')
    axes[1].set_title('Нормальное распределение', size=20)
    axes[1].legend(['Количество частиц'])

    plt.show()
