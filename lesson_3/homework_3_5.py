# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

fib_1, fib_2 = 0, 1
fib_list = [1, 0, 1]

n = int(input("Введите индекс числа Фибоначчи: "))

for i in range(2, n + 1):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    fib_list.insert(i * 2, fib_2)
    fib_list.insert(-(i * 2), fib_2 * (-1) ** (i - 1))

print(fib_list)
