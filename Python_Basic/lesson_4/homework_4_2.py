# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа. Простые делители числа онлайн
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]


def simple_mount(my_number):
    divider_list = []
    for value in range(2, int(my_number / 2)):
        while not my_number % value:
            divider_list.append(value)
            my_number /= value

    return divider_list


user_number = int(input("Enter number: "))
print(simple_mount(user_number))
