# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
# out in the file
# 3*x ^ 9 + 3*x ^ 8 - 2*x ^ 6 + 1*x ^ 5 - 3*x ^ 4 - 3*x ^ 2 + 3 = 0
# 4*x ^ 5 + 1*x ^ 4 - 3*x ^ 3 - 3 = 0
# 4*x ^ 2 - 4 = 0
# in
# 0
# -1
# 4
# out in the file
# 3*x ^ 9 + 3*x ^ 8 - 2*x ^ 6 + 1*x ^ 5 - 3*x ^ 4 - 3*x ^ 2 + 3 = 0
# 4*x ^ 5 + 1*x ^ 4 - 3*x ^ 3 - 3 = 0
# 4*x ^ 2 - 4 = 0
# 2*x ^ 4 - 3*x ^ 3 + 3*x ^ 2 + 1*x ^ 1 - 2 = 0


import random as r


def rdm_odds():
    new_odd = int(r.random()*5) * 2
    return new_odd


def gen_polynom(user_power):
    result = ''

    for elem in range(0, user_power + 1, 1):
        odd_sign = ' - '
        koeff = rdm_odds()
        diff = user_power - elem
        str_x = '*x ^ '

        if koeff == 0:
            koeff = ''
            odd_sign = ''
            str_x = ''
            diff = ''

        elif koeff == 1:
            koeff = ''
            str_x = 'x ^ '

        else:
            if elem == 0:
                odd_sign = ''
                str_x = '*x ^ '

            elif elem:
                odd_sign = ' + '

                if diff == 1:
                    odd_sign = ' + '
                    str_x = 'x '
                    diff = ''

                elif diff == 0:
                    odd_sign = ' - '
                    str_x = ''
                    diff = ''

        result += f"{odd_sign}{koeff}{str_x}{diff}"

    return result + ' = 0'


if __name__ == "__main__":

    def write_in_file(my_number):
        with open('newfile.txt', 'a', encoding='utf-8') as f:
            f.write(f'{gen_polynom(my_number)}\n')

    for i in range(3):
        pow_number = int(input('Задайте натуральную степень k:'))
        if pow_number < 0:
            pow_number *= (- 1)
        write_in_file(pow_number)
