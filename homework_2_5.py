# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]


my_number = int(input("Input any number, please: "))
if my_number < 0:
    my_number *= -1

my_list = [*range(my_number)]
print(my_list)

for int_div in range(len(my_list)):
    place_number = int((int_div * 7) % 10)
    if place_number <= len(my_list):
        my_list.append(my_list.pop(place_number))

print(my_list)
