# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


N = abs(int(input()))
def FibonachiPos (n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        Numbers = FibonachiPos(n-1) + FibonachiPos(n-2)
    return Numbers

negN = -1 * N
def FibonachiNeg (n):
    if n == 0:
        return 0
    elif n == -1:
        return 1
    else:
        Numbers = FibonachiNeg(n+2) - FibonachiNeg(n+1)
        return Numbers
list_fib = []
for i in range (negN, -1):
   list_fib.append(FibonachiNeg(i))

for j in range (N+1):
   list_fib.append(FibonachiPos(j)) 
print(list_fib)