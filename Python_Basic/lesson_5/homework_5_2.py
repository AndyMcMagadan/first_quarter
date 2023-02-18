# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


# text_file = input('Enter the name of the file with the text: ')
text_file = 'text_words.txt'
# user_string = input('Enter the strimg of the text: ')
user_string = f'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa\nvvvvvvvvvvvbbwwPPuuuTTYyWWQQ'
# print(user_string)

with open(text_file, 'w', encoding='utf-8') as t_f:
    t_f.write(user_string)

with open(text_file, 'r', encoding='utf-8') as r_f:
    my_data = r_f.read()

print(my_data)

my_list = list(my_data)
start_elem = my_list.pop(0)
counter = 1
code_string = ''
short_code_string = ''

while my_list:
    elem = my_list.pop(0)
    counter += 1

    if elem == start_elem:
        short_code_string = f'{str(counter)}{elem}'

    else:
        start_elem = elem
        counter = 1
        code_string += short_code_string
        short_code_string = ''

short_code_string = f'{str(counter)}{elem}'
code_string += short_code_string

# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# code_file = input('Enter the file name to record: ')
code_file = 'text_code_words.txt'
# decode_file = input('Enter the name of the file to decode: ')
decode_file = 'text_code_words.txt'

with open(code_file, 'w', encoding='utf-8') as c_f:
    c_f.write(code_string)

with open(decode_file, 'r', encoding='utf-8') as c_r_f:
    code_data = c_r_f.read()

print(code_data)
