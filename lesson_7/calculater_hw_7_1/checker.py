def check_of_num(data):
    if data.replace('.', '').isdigit():
        return float(data)
    else:
        return f'Entered incorrectly. Try again!'
