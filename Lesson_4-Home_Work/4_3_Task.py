# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
import sys
size_list = int(input("Введите размер последовательности: "))
if size_list <= 1:
    print("Вы ввели размер, не позволяющий сформировать последовательность")
    sys.exit()

def create_random_list(size_order):
    list_order = []
    from random import randrange
    for i in range(0, size_order):
        list_order.append(randrange(0, 10))
    return list_order
random_list = create_random_list(size_list)
print(random_list)

def create_random_list(list_order, size_order):
    list_non_repeat = []
    for j in range(0, size_order):
        count_elem = list_order.count(list_order[j])
        if count_elem == 1:
            list_non_repeat.append(list_order[j])
    return list_non_repeat
list_non_rep = create_random_list(random_list, size_list)
print(list_non_rep)