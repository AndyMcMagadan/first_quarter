# * 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

def draw_field(user_list):

    print(f'------------')
    print(f'| {user_list[0]} | {user_list[1]} | {user_list[2]} |')
    print(f'------------')
    print(f'| {user_list[3]} | {user_list[4]} | {user_list[5]} |')
    print(f'------------')
    print(f'| {user_list[6]} | {user_list[7]} | {user_list[8]} |')
    print(f'------------')


def check_win(user_name, word):
    win_list = ['abc', 'def', 'ghi', 'adg', 'beh', 'cfi', 'aei', 'ceg']
    for elem in win_list:
        counter = 0
        for e in elem:
            if e in word:
                counter += 1
                if counter == 3:
                    return f'{user_name} is winner!'


list_args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
draw_field(list_args)


cross_word = ''
zero_word = ''
win_sign = False
my_count = 0

while not win_sign:
    field_name_cross = input('Enter field name for CROSS (X): ')
    if field_name_cross in list_args:
        index_cross = list_args.index(field_name_cross)
        list_args[index_cross] = 'X'
    else:
        print('The field is occuped. Try again next time.')

    draw_field(list_args)
    cross_word += field_name_cross

    my_cross_word = ''.join(sorted(cross_word))
    result = check_win('Cross', my_cross_word)
    if result:
        print(result)
        win_sign = True
        if win_sign == True:
            break

    my_count += 1
    if my_count >= 8:
        print('Nobody win!')
        break

    field_name_zero = input('Enter field name for ZERO (0): ')
    if field_name_zero in list_args:
        index_zero = list_args.index(field_name_zero)
        list_args[index_zero] = '0'
    else:
        print('The field is occuped. Try again next time.')

    draw_field(list_args)
    zero_word += field_name_zero

    my_zero_word = ''.join(sorted(zero_word))
    result = check_win('Zero', my_zero_word)
    if result:
        print(result)
        win_sign = True

    my_count += 1
    if my_count >= 8:
        print('Nobody win!')
        break
