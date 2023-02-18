# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.

# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

my_number = input("Input any number, please: ")
sum_number = 0
power_number = len(my_number) - 2
my_number = float(my_number)
my_number *= int(10 ** power_number)

while my_number:
    sum_number += int(my_number % 10)
    my_number //= 10

print(sum_number)
