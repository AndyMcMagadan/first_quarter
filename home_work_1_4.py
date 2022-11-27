# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
# координат точек в этой четверти(x и y).
# *Пример: *
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

num_quarter = int(input('Input number of quarter: '))

if num_quarter == 1:
    print('x > 0 and y > 0')
elif num_quarter == 2:
    print('x < 0 and y > 0')
elif num_quarter == 3:
    print('x < 0 and y < 0')
elif num_quarter == 4:
    print('x > 0 and y < 0')
else:
    print('No such quarter!')
