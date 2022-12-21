# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

number = float(input("Введите вещественное число: "))
if number < 0:
    number *= -1
number_whole = int(number)
lenght_number_whole = len(str(number_whole))
lenght_number_fraction = len(str(number)) - len(str(number_whole)) - 1
number_fraction = round(number - number_whole, lenght_number_fraction)
number_fraction_new = number_fraction * 10 ** lenght_number_fraction

def get_sum(lenght_number, number):
    sum = 0
    for i in range(1, lenght_number + 1):
        interm = int(int(number % (10**i)) / int(10**(i - 1)))
        sum += interm
    return sum

# print(number_whole)#промежуточные выводы для визуализации этапов при решении
# print(number_fraction)
# print(lenght_number_whole)
# print(lenght_number_fraction)
sum = get_sum(lenght_number_whole, number_whole) + get_sum(lenght_number_fraction, number_fraction_new)
print("Сумма цифр введенного числа: ", sum)


