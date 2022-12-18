# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

list1 = []
for i in range(int(input())):
    list1.append(i)
print(list1)
from random import randint
for i in range(len(list1)):
    term = list1[i]
    j = randint(0, len(list1) - 1)
    list1[i] = list1[j]
    list1[j] = term
print(list1)


    