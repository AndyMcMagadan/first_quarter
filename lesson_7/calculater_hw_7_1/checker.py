from logger import logging


def check_of_num(data):
    try:
        data.replace('.', '', 1).isdigit()
        print('Is Digit!')
        return float(data)
    except:
        logging.warning(f'Incorrect data entered {data}!')
        return f'Entered incorrectly. Try again!'
