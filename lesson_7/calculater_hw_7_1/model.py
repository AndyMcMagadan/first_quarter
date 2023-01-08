def sum(x_1, x_2, y_1, y_2):
    return f'result = {x_1 + y_1} + {(x_2 + y_2)}*j'


def sub(x_1, x_2, y_1, y_2):
    return f'result = {x_1 - y_1} + {(x_2 - y_2)}*j'


def mult(x_1, x_2, y_1, y_2):
    return f'result = {x_1 * y_1} + {x_1 * y_2 + x_2 * y_1}*j + {(x_2 + y_2)}*j^2'


def div(x_1, x_2, y_1, y_2):
    return f'result = {(x_1 * x_2 + y_1 * y_2)/(x_2 ** 2 + y_2**2)} + {(x_2 * y_1 - x_1 * y_2)/ (x_2 ** 2 + y_2**2)}*j'


def sum_real(x_1, y_1):
    return f'result = {x_1 + y_1}'


def sub_real(x_1, y_1):
    return f'result = {x_1 - y_1}'


def mult_real(x_1, y_1):
    return f'result = {x_1 * y_1}'


def div_real(x_1, y_1):
    return f'result = {x_1 / y_1}'


def int_div(x_1, y_1):
    return f'result = {x_1//y_1}'


def rem_div(x_1, y_1):
    return f'result = {x_1//y_1}'


def power(x_1, y_1):
    return f'result = {x_1**y_1}'


def sqrt(x_1):
    return f'result = {x_1**(0.5)}'
