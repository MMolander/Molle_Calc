"""
Our terminal user interface
"""
from Src.calc import add, div


# Desired operation:
# Input your expression below:
# > 1 + 2
# 3


def main(expression):
    if "+" in expression:
        [input_1, input_2] = expression.split("+", maxsplit=1)
        num_1 = float(input_1)
        num_2 = float(input_2)
        return add(num_1, num_2)
    elif "/" in expression:
        [input_1, input_2] = expression.split("/", maxsplit=1)
        num_1 = float(input_1)
        num_2 = float(input_2)
        return div(num_1, num_2)
    else:
        raise NotImplementedError("Math operator not implemented.")


# Was invoked as a program/script.
if __name__ == "__main__":
    while True:
        try:
            print("Input your expression below:")
            user_input = input("> ")
            result = main(user_input)
            print(result)
        except ZeroDivisionError as err:
            print("Division by zero not allowed, please try again")
        except ValueError as err:
            print(err)

