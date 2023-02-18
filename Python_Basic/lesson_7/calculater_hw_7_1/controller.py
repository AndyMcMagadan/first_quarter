import model
import view
import checker
from logger import logging


def main_value():
    value = view.get_value()
    result = checker.check_of_num(value)
    return result


def main_menu():
    while True:
        # value = 0
        print('\nWorking with:\n1 - rational\n2 - complex\n0 - exit')
        # value = view.get_value()
        result = int(main_value())
        if result == 1:
            menu_real()
        elif result == 2:
            menu_complex()
        elif not result:
            logging.info('Stop programm')
            print('Goodbye! See You later!')
            exit()
        else:
            logging.warning('Wrong item')
            print('One more')


def menu_real():
    print('Working with:\n1 - sum\n2 - sub\n3 - mult\n4 - div\n5 - pow\n6 - //\n7 - %\n8 - sqrt\nOther - Main menu')
    result = main_value()
    print('Enter 1 number', end=' ')
    x_1 = main_value()
    print('Enter 2 number', end=' ')
    y_1 = main_value()
    # print('Rational', result, x_1, y_1)
    if result == 1:
        result = model.sum_real(x_1, y_1)
        view.my_result(result)
    elif result == 2:
        result = model.sub_real(x_1, y_1)
        view.my_result(result)
    elif result == 3:
        result = model.mult_real(x_1, y_1)
        view.my_result(result)
    elif result == 4:
        result = model.div_real(x_1, y_1)
        view.my_result(result)
    elif result == 5:
        result = model.power(x_1, y_1)
        view.my_result(result)
    elif result == 6:
        result = model.int_div(x_1, y_1)
        view.my_result(result)
    elif result == 7:
        result = model.rem_div(x_1, y_1)
        view.my_result(result)
    elif result == 8:
        result = model.sqrt(x_1)
        view.my_result(result)
    else:
        main_menu()


def menu_complex():
    print('Working with:\n1 - sum\n2 - sub\n3 - mult\n4 - div\nOther - Main menu')
    result = main_value()
    print('Enter real part 1 number', end=' ')
    x_1 = main_value()
    print('Enter imaginary part 1 number', end=' ')
    x_2 = main_value()
    print('Enter real part 2 number', end=' ')
    y_1 = main_value()
    print('Enter imaginary part 2 number', end=' ')
    y_2 = main_value()
    if result == 1:
        result = model.sum(x_1, x_2, y_1, y_2)
        view.my_result(result)
    elif result == 2:
        result = model.sub(x_1, x_2, y_1, y_2)
        view.my_result(result)
    elif result == 3:
        result = model.mult(x_1, x_2, y_1, y_2)
        view.my_result(result)
    elif result == 4:
        result = model.div(x_1, x_2, y_1, y_2)
        view.my_result(result)
    else:
        main_menu()
