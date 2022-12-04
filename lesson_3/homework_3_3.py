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
        bin_list.append(int(my_number % 2))
        my_number //= 2
    return bin_list


user_number = int(input("Ввведите число: "))

bin_view = [str(i) for i in dec_in_bin(user_number)]
bin_view.reverse()
print("".join(bin_view))
