# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Xa = int(input("Enter coordinate Xa: "))
Ya = int(input("Enter coordinate Ya: "))
Xb = int(input("Enter coordinate Xb: "))
Yb = int(input("Enter coordinate Yb: "))
from math import sqrt
print(round(sqrt((Xb - Xa) ** 2 + (Yb - Ya) ** 2), 3))