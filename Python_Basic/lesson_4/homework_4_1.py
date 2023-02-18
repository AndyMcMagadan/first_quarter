# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988


def accuracy_number(my_number, my_accuracy):
    len_accuracy = len(my_accuracy) - 2
    my_number = float(my_number)
    return f"{my_number:.{len_accuracy}f}"


user_number = input('Enter a real number: ')
user_accuracy = input('Enter the required accuracy: ')

print(accuracy_number(user_number, user_accuracy))
