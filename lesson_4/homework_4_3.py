# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import choices


def list_create(mount):
    return choices(range(10), k=mount)


def unical_many(my_list):
    new_list = []
    new_list_1 = []
    for k in range(len(my_list)):
        elem = my_list.pop(0)
        if elem not in my_list and elem not in new_list_1:
            new_list.append(elem)
        else:
            new_list_1.append(elem)

    # print(new_list_1)
    return new_list


user_number = int(input("Enter number: "))
if user_number >= 0:
    new_list = list_create(user_number)
    print(new_list)
    print(unical_many(new_list))
else:
    print('Negative value of the number of numbers!')
