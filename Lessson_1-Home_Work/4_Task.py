# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
num = int(input("Enter the quarter number: "))
if num == 1:
    print("X > 0, Y > 0")
elif num == 2:
    print("X < 0, Y > 0")
elif num == 3:
    print("X < 0, Y < 0")
elif num == 4:
    print("X > 0, Y < 0")
else:
    print("The quarter is intered incorrectly")
1