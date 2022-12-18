# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
n = int(input("Введите положительное  число: "))
list_number = []
if n < 1:
    print("Вы ввели ноль или отрицательное число, введите чило заново")
else:
    term = 0
    for i in range(1, n + 1):
        term = round((1 + 1 / i) ** i, 3)
        list_number.append(term)
    print(list_number)
    sum = 0
    for j in range(0, n):
        sum += list_number[j]
    print(sum)