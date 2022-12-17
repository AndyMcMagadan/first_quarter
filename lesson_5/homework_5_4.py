# ** 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

count_of_candies = 2021
gamer_1, gamer_2 = input('Введите имя 1 игрока: '), 'Myghty bot'
current_gamer = gamer_1
print(f'Количество оставшихся конфет: {count_of_candies}')
while count_of_candies > 0:

    while True:
        number_to_delete = int(
            input(f'Ход игрока {current_gamer} (1 - 28): '))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break

    count_of_candies -= number_to_delete
    if count_of_candies == 0:
        break

    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2

    print(f'Количество оставшихся конфет: {count_of_candies}')
    if count_of_candies > 57:
        multy = count_of_candies // 28
        number_to_delete = count_of_candies - multy * 28 - 1
    elif 57 >= count_of_candies > 28:
        number_to_delete = count_of_candies - 28 - 1
        if number_to_delete == 0:
            number_to_delete = 1
    else:
        number_to_delete = count_of_candies

    print(f'Ход игрока {current_gamer} (1 - 28): {number_to_delete}')
    count_of_candies -= number_to_delete
    current_gamer = gamer_1 if current_gamer == gamer_2 else gamer_2

    print(f'Количество оставшихся конфет: {count_of_candies}')

print(f'Победил {gamer_1 if current_gamer == gamer_2 else gamer_2}')
