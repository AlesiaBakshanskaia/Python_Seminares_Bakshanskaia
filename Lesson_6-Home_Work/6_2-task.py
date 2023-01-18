# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
import sys
N = int(input('Введите число N: '))
if N < 20:
    print("Вы ввели не верное число")
    sys.exit()

def sort_div_20_21(num):
    list_20_num = [i for i in range(20, num+1) if i % 20 == 0 or i % 21 == 0]
    return list_20_num
list_20_N = sort_div_20_21(N)
print(list_20_N)