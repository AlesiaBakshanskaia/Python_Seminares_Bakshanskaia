# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
from random import sample

def create_random_list (size):
    random_list = sample(range(1, size*3 + 1), size)
    return random_list
random_list = create_random_list(abs(int(input("Enter the number of numbers in the list: "))))
print(random_list)

sum_element = 0
for i in range(0, len(random_list), 2):
    sum_element += random_list[i]
print(sum_element)
