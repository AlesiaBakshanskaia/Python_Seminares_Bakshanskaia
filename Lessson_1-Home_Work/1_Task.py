# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Day_week = int(input("Enter the day of the week as a number: "))
if Day_week > 0 and Day_week < 6:
    print("It's a workday")
elif Day_week == 6 or Day_week == 7:
    print("It's a weekend")
else:
    print("It's not a day of the week")
