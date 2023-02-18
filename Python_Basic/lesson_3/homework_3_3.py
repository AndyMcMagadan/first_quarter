# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011


def dec_in_bin(my_number):
    bin_list = []
    while my_number:
        bin_list.insert(0, int(my_number % 2))
        my_number //= 2
    return bin_list


user_number = dec_in_bin(int(input("Ввведите число: ")))

print(*user_number, sep='')
