# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
X = int(input("Enter coordinate X: "))
Y = int(input("Enter coordinate Y: "))
if X > 0 and Y > 0:
    print("This is the first quarter")
elif X < 0 and Y > 0:
    print("This is the second quarter")
elif X < 0 and Y < 0:
    print("This is the third quarter")
elif X > 0 and Y < 0:
    print("This is the fourth quarter")
elif X == 0 and Y != 0:
    print("This is the x axis")
elif X != 0 and Y == 0:
    print("This is the y axis")
else:
    print("This is the origin of coordinates")