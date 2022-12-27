# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
number = int(input("Enter number: "))

list_numbers = []
while number:
    list_numbers.append(str(number%2))
    number //= 2
# print(list_numbers)
list_numbers.reverse()
# print(list_numbers)
number_in_2 = int("".join(list_numbers))
print(number_in_2)