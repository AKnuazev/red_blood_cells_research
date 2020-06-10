from source.graphs import make_dists, make_Imin_graphs

# Получаем данные от пользователя
# print("Enter R:")   # Выводим в консоль просьбу ввести данные
# R = input() # Считываем введенные до нажатия ENTER данные в перемнную
#
# print("Enter N:") # Выводим в консоль просьбу ввести данные
# N = int(input()) # Считываем введенные до нажатия ENTER данные в перемнную

N = 1000

make_dists(N)
make_Imin_graphs(N)
