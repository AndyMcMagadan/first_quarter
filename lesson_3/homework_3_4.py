# 4. * Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной
# части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform


def list_create(mount):
    new_list = []
    for i in range(mount):
        new_list.append(round(uniform(0.01, 9.99), 2))
    return new_list


def find_diff(my_list):
    new_list = []
    for elem in my_list:
        new_elem = round(elem % 1, 2)
        new_list.append(new_elem)
    return new_list


def find_max(my_list):
    max_value = 0
    for elem in my_list:
        if elem > max_value:
            max_value = elem
    return max_value


def find_min(my_list):
    min_value = 1
    for elem in my_list:
        if elem < min_value:
            min_value = elem
    return min_value


user_list = list_create(int(input("Введите количество элементов списка: ")))
print(user_list)

diff_list = find_diff(user_list)
max_list = find_max(diff_list)
min_list = find_min(diff_list)

print(
    f"Разница между максимальным {max_list} и минимальным значением {min_list}\nдробной части элементов составляет: {max_list - min_list}"
)
