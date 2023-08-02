import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO
)

def divide_num(num1, num2):
    result = 0
    try:
        result =  num1 / num2
    except ZeroDivisionError as e:
        logging.exception(str(e))
    except TypeError as e:
        print("TypeError: Input must be integer or float")
    except OverflowError as e:
        logging.exception(str(e))
    else:
        print("Done")
