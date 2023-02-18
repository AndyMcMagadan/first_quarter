# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect


from random import randint


def gen_string():
    user_number = int(input('Enter of Number of words: '))
    symbol_list = ['а', 'б', 'в']
    total_string = ''
    for ind in range(user_number):
        short_string = ''
        for _ in range(3):
            numer = int(randint(0, 8) / 3)
            simbol = symbol_list[numer]
            short_string += simbol
        total_string += short_string
        if ind + 1 != user_number:
            total_string += ' '
    return total_string


user_str = gen_string()
print(user_str)
user_str = user_str.replace('абв', '')
user_str = user_str.replace('  ', ' ')
print(user_str)
