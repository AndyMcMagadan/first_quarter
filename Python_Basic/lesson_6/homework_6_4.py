# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
# out
# {'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
# 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
# И': {'И': ['Илья Иванов']}, 'В': {'Ю': ['Юнона Ветрякова']}}


def gen_short_dict(key, user_list):
    short_dict = {}
    for elem in user_list:
        if elem[0] == key:
            if elem[1] not in short_dict:
                short_dict[elem[1]] = [elem[2]]
            else:
                short_dict[elem[1]].append(elem[2])

    return short_dict


name_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
             "Анна Савельева", "Юнона Ветрякова", "Борис Аркадьев", "Антон Серов", "Павел Анисимов"]

set_key_1 = set([name.split()[1][0] for name in name_list])

user_list = [[name.split()[1][0], name.split()[0][0], name]
             for name in name_list]

# Way 1
total_dict = {key_1: gen_short_dict(key_1, user_list) for key_1 in set_key_1}
print(f'Way 1:\n{total_dict}')

# Way 2
for key_1 in set_key_1:
    total_dict[key_1] = gen_short_dict(key_1, user_list)
print(f'Way 2:\n{total_dict}')
