# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import choices


def list_create(mount):
    return choices(range(50), k=mount)


def multi_elem(my_list):
    multi_list = []
    for key in range(1, int((len(my_list) + 3) / 2)):
        if (key) < (len(my_list) - key):
            multi_list.append(my_list[(key - 1)] * my_list[(len(my_list) - key)])
        else:
            multi_list.append(my_list[key - 1])
    return multi_list


user_number = int(input("Enter number: "))
new_list = list_create(user_number)
print(new_list)
print(multi_elem(new_list))
