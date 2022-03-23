def addition(num1, num2):
    return num1+num2


def subtraction(num1, num2):
    return num1-num2


def multiplication(num1, num2):
    return num1*num2


def division(num1, num2):
    try:
        return num1/num2
    except (ZeroDivisionError, TypeError) as err:
        return err
