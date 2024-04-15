import logging
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL



def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

num1 = 11
num2 = 4
'''
add_result = add(num1, num2)
logging.debug(f'{num1} + {num2} = {add_result}')
subtract_result = subtract(num1, num2)
logging.debug(f'{num1} - {num2} = {subtract_result}')


# changing the default level of logging
logging.basicConfig(level=logging.DEBUG)

multiply_result = multiply(num1, num2)
logging.debug(f'{num1} * {num2} = {multiply_result}')
divide_result = divide(num1, num2)
logging.debug(f'{num1} / {num2} = {divide_result}')
'''
# Writing lig statements to a file with a time stamp
logging.basicConfig(filename='log_sample.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

add_result = add(num1, num2)
logging.debug(f'{num1} + {num2} = {add_result}')
subtract_result = subtract(num1, num2)
logging.debug(f'{num1} - {num2} = {subtract_result}')
