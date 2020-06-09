from source.graphs import make_ravn_dists, make_dists

# Получаем данные от пользователя
print("Enter R:")   # Выводим в консоль просьбу ввести данные
R = input() # Считываем введенные до нажатия ENTER данные в перемнную

print("Enter N:") # Выводим в консоль просьбу ввести данные
N = int(input()) # Считываем введенные до нажатия ENTER данные в перемнную


make_dists(N)