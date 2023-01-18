# ** 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

mode_game = int(input("Для выбора режима игры введите 0 (человек бот) или 1 (человек человек): "))
import sys
if 1 > mode_game < 0:
    print("Вы выбрали несуществующий режим")
    sys.exit()

from random import randint
if mode_game:
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
else:
    player1 = input("Введите имя первого игрока: ")
    player2 = "Бот"
allsweets = 121
priority = randint(0, 1)

if priority:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

def input_sweets(name):
    sweets = int(input(f"{name}, введите количество конфет, которое вы возьмете от 1 до 28: "))
    while sweets < 1 or sweets > 28:
        sweets = int(input(f"{name}, введите корректное количество конфет: "))
    return sweets

def print_results(name, num,  allsweets):
    print(f"{name} взял {num}, осталось  {allsweets} конфет.")

while allsweets > 28:
    if priority:
        num = input_sweets(player1)
        allsweets -= num
        priority = False
        print_results(player1, num, allsweets)
    else:
        if mode_game:
            num = input_sweets(player2)
        else:
            num = allsweets % 29
        allsweets -= num
        priority = True
        print_results(player2, num, allsweets)
if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")