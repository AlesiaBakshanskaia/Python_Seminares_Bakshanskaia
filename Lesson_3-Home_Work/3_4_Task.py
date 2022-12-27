# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
from random import uniform

def create_random_list (size):
    random_list = []
    for i in range(size):
        num = round(uniform(0, 10), 2)
        random_list.append(num)
    return random_list
random_list = create_random_list(abs(int(input("Enter the number of numbers in the list: "))))
print(random_list)

def del_int (r_list):
    fract_list = []
    for i in range(len(r_list)):
        fract_list.append(round(float(r_list[i]) - int(r_list[i]), 2))
    return fract_list
fraction_list = del_int (random_list)
# print(fraction_list)

print("Max: ", max(fraction_list))
print("Min: ", min(fraction_list))

differ = max(fraction_list) - min(fraction_list)
print("Difference: ", differ)