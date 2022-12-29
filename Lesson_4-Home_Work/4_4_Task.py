# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# import random
# def rnd():
#     return random.randint(0, 11)
# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)  
# print(create_mn(k))
k = int(input("Введите натуральную степень к: "))
if k <= 0:
    print("Вы ввели не натуральную степень")
    sys.exit()

def create_random_list(size_order):
    list_order = []
    from random import randrange
    for i in range(0, size_order+1):
        list_order.append(randrange(0, 10))
    return list_order
list_koef = create_random_list(k)
print(list_koef)

polynomial = ""
for i in range(k+1):
    if i <= k - 2 and list_koef[i] != 0:
        polynomial += f"{list_koef[i]}*x^{k-i}"
        if list_koef[i] > 0:
            polynomial += " + "
    elif i == k - 1 and list_koef[i] != 0:
        polynomial += f"{list_koef[i]}*x"
        if list_koef[i+1] > 0:
            polynomial += " + "
    elif i ==k and  list_koef[i] != 0:
        polynomial += f"{list_koef[i]}"
polynomial += " = 0 "
print(polynomial)

with open ("Poly2.txt", "a") as fileP:
    fileP.writelines(polynomial)