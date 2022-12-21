# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

number = int(input("Введите положительное  число: "))
list_multiplication = []
if number < 1:
    print("Вы ввели ноль или отрицательное число, введите чило заново")
else:
    term = 1
    for i in range(1, number + 1):
        term *= i
        list_multiplication.append(term)
    print(list_multiplication)
