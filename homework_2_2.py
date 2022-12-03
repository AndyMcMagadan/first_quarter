# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


my_number = int(input("Input any number, please: "))
my_list = []
new_number = 1

for i in range(1, my_number + 1):
    new_number *= i
    my_list.append(new_number)

print(my_list)
