# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekends = [6, 7]
day_for_checkit = int(input('Введите день недели: '))
if day_for_checkit > 7 or day_for_checkit <= 0:
    print('This number is a mistake in weekdays!')
elif day_for_checkit in weekends:
    print("Yes, it's weekend.")
else:
    print("No, it's regular day.")
