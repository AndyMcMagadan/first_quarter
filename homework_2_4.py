# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне[-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

my_number = int(input("Enter the value of N: "))
number_1 = int(input("Input position one, please: "))
number_2 = int(input("Input position two, please: "))

new_list = []
if my_number >= 0:
    for i in range(-my_number, my_number + 1):
        new_list.append(i)
else:
    for i in range(my_number, -my_number + 1):
        new_list.append(i)

print(f"Position one: {number_1}")
print(f"Position two: {number_2}")
print(new_list)

if number_1 > len(new_list):
    print("There are no values for these indexes!")
elif number_2 > len(new_list):
    print("There are no values for these indexes!")
else:
    print(new_list[number_1] * new_list[number_2])
