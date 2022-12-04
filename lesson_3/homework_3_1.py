# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import choices


def list_create(mount):
    return choices(range(30), k=mount)


def sum_odd_elem(my_list):
    sum_elem = 0
    for key, elem in enumerate(my_list):
        if not key % 2:
            sum_elem += elem
    return sum_elem


new_list = list_create(int(input("Введите количество элементов списка: ")))
print(f"Сумма нечетных элементов {new_list}:\n {sum_odd_elem(new_list)}")
