# 3. Задайте список из n чисел, заполненный по формуле(1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071


my_number = int(input("Input any number, please: "))
new_list = []
multy_num = 1

for n in range(1, my_number + 1):
    new_number = (1 + 1 / n) ** n
    new_list.append(round(new_number, 3))
    multy_num += round(new_number, 3)

print(f"Список из {my_number} значений: {new_list}\n Сумма значений списка: {multy_num - 1}")
