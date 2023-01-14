# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number  = int(input("Введите натуральное число: "))


def create_list_simp_multip(num: int) -> list:
   i = 2
   list_simp_multip = []
   while i * i <= num:
       while num % i == 0:
           list_simp_multip.append(i)
           num //= i
       i = i + 1
   if num > 1:
       list_simp_multip.append(num)
   return list_simp_multip

print(create_list_simp_multip(number))

