# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]


def list_comprehension(user_list):
    result = [user_list[n]
              for n in range(len(user_list)) if n > 0 and user_list[n] > user_list[n - 1]]
    return result


user_list_1 = [15, 16, 2, 3, 1, 7, 5, 4, 10]
print(user_list_1)
print(list_comprehension(user_list_1))

user_list_2 = [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
print(user_list_2)
print(list_comprehension(user_list_2))
