# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
import sys
from random import sample


def create_list(size_list):
    cr_list = sample(range(1, 101), size_list)
    return cr_list


size_list = int(input('Введите размер списка: '))
if size_list < 1:
    print("Вы выбрали несуществующий режим")
    sys.exit()

new_list = create_list(size_list)
print(new_list)


def change_list(some_list):
    some_list = [new_list[i] \
        for i in range(1, len(new_list)) if new_list[i] > new_list[i-1]]
    return some_list

res_list = change_list(new_list)
print(res_list)
