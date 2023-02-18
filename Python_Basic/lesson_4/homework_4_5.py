# ** 5. Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
# out in the file
# 3*x ^ 9 + 3*x ^ 8 - 2*x ^ 6 + 1*x ^ 5 - 3*x ^ 4 - 3*x ^ 2 + 3 + 2*x ^ 2 + 2*x ^ 1 + 2 = 0
# 4*x ^ 5 + 1*x ^ 4 - 3*x ^ 3 - 3 + 3*x ^ 3 - 4*x ^ 2 - 2*x ^ 1 - 4 = 0
# 4*x ^ 2 - 4 + 3*x ^ 6 - 4*x ^ 5 - 4*x ^ 4 - 4*x ^ 3 + 3*x ^ 2 - 2*x ^ 1 - 0 = 0
# in
# "poly.txt"
# "poly_2.txt"
# out
# The contents of the files do not match!


import random as r
from homework_4_4 import gen_polynom


def file_name(my_number):
    f_name = f'poly_{my_number + 1}.txt'
    f_n = f'f_{my_number + 1}'
    return f_name, f_n


def fill_lists(word):

    power_list = []
    koeff_list = []
    for key, value in enumerate(word):

        if key == 0 and value == '+':
            value = '1'

        elif key > 0 and value == '+':
            power_list.append(int(word[key - 1]))
            koeff_list.append(int((word[key - 3])[0]))

        elif key > 0 and value == '-':
            if word[key - 2][1]:
                power_list.append(1)
                koeff_list.append(int((word[key - 2])[0]))
            else:
                power_list.append(0)
                koeff_list.append(int((word[key - 3])))

        elif key > 0 and value == '=':
            if word[key - 1]:
                power_list.append(0)
                koeff_list.append(int((word[key - 1])[0]))

    return power_list, koeff_list


def gen_sum_polynom(c_p_list, s_list):
    new_polynom = ''
    for ind, pow in enumerate(c_p_list):
        str_x = '*x ^ '
        sign = ' + '
        if len(c_p_list) - ind - 1 == 0:
            str_x = ''
            pow = ''
            sign = ''
        elif len(c_p_list) - ind - 2 == 0:
            str_x = 'x'
            pow = ''
            sign = ' - '
        new_polynom += f'{s_list[ind]}{str_x}{pow}{sign}'

    new_polynom += ' = 0'
    return new_polynom


word_1 = word_2 = []
for ind in range(2):
    pow_number = r.randint(5, 9)
    result = file_name(ind)
    f_name, f_n = result[0], result[1]

    with open(f_name, 'w', encoding='utf-8') as f_n:
        f_n.write(f'{gen_polynom(pow_number)}\n')

    with open(f_name, 'r', encoding='utf-8') as f_n:

        if not word_1:
            word_1 = f_n.read().strip()
            print(word_1)
            word_1 = word_1.split(' ')
        else:
            with open(f_name, 'r', encoding='utf-8') as f_n:
                word_2 = f_n.read().strip()
                print(word_2)
                word_2 = word_2.split(' ')

# print(f'{word_1},\n{word_2}')
result_1 = fill_lists(word_1)
result_2 = fill_lists(word_2)

power_list_1 = result_1[0]
koeff_list_1 = result_1[1]

power_list_2 = result_2[0]
koeff_list_2 = result_2[1]

# print(f'{power_list_1}  {power_list_2}, \n{koeff_list_1}  {koeff_list_2}')

if max(power_list_2) > max(power_list_1):
    common_max = max(power_list_2)
else:
    common_max = max(power_list_1)

common_pow_list = []
sum_list = []

for power in range(common_max + 1):

    if (power in power_list_1) and (power in power_list_2):
        ind_koeff_1 = power_list_1.index(power)
        ind_koeff_2 = power_list_2.index(power)
        sum_koeff = koeff_list_1[ind_koeff_1] + koeff_list_2[ind_koeff_2]
        common_pow_list.insert(0, power)
        sum_list.insert(0, sum_koeff)
    elif (power in power_list_1):
        ind_koeff_1 = power_list_1.index(power)
        sum_koeff = koeff_list_1[ind_koeff_1]
        common_pow_list.insert(0, power)
        sum_list.insert(0, sum_koeff)
    elif (power in power_list_2):
        ind_koeff_2 = power_list_2.index(power)
        sum_koeff = koeff_list_2[ind_koeff_2]
        common_pow_list.insert(0, power)
        sum_list.insert(0, sum_koeff)

# print(common_pow_list, sum_list)

result = gen_sum_polynom(common_pow_list, sum_list)
print(result)

with open('sum_poly.txt', 'w', encoding='utf-8') as f_sum:
    f_sum.write(result)
