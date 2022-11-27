# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.
# https: // ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

# out
# 5.099


import math


x1 = int(input('Input "X1": '))
y1 = int(input('Input "Y1": '))
x2 = int(input('Input "X2": '))
y2 = int(input('Input "Y2": '))

z = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 4)
print(z)
