# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample
def create_random_list (size):
    random_list = sample(range(1, size*3 + 1), size)
    return random_list

random_list = create_random_list(abs(int(input("Enter the number of numbers in the list: "))))
print(random_list)

def create_pair_list (r_list):
    pair_list = []
    for i in range(int(len(r_list)/2)):
        pair_list.append(r_list[i]*r_list[-1-i])
    if len(r_list) % 2 != 0:
            pair_list.append(r_list[int(len(r_list)/2)])
    return   pair_list  

res_pair_list = create_pair_list (random_list)
print(res_pair_list)