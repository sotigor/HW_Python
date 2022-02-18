"""Create a function called make_operation, which takes in a simple arithmetic operator
as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
and an arbitrary number of arguments (only numbers) as the second parameter.
Then return the sum or product of all the numbers in the arbitrary parameter."""


def make_operation_1(sign, num1, num2, num3=0, num4=0):
    """Calculate and return the result of mathematical operations

    Use following signs ‘+’, ‘-’ or ‘*’ between the given numbers
    """
    if sign == "+":
        return num1 + num2 + num3 + num4
    elif sign == "-":
        return - num1 - num2 - num3 - num4
    elif sign == "*":
        return num1 * num2 * num3 * num4
    else:
        return 'Passed sign is incorrect'


def make_operation_2(*args):
    """Calculate and return the result of mathematical operations

    Use following signs ‘+’, ‘-’ or ‘*’ between the given numbers
    Handle with any amount of numbers
    """
    result = 0
    result_1 = 1
    for item in args[1:]:
        if args[0] == "+":
            result += item
        elif args[0] == "-":
            result -= item
        elif args[0] == "*":
            result_1 *= item
        else:
            return 'Passed sign is incorrect'
    return result if args[0] != '*' else result_1


print(make_operation_1('+', 7, 7, 2), make_operation_2('+', 7, 7, 2))
print(make_operation_1('-', 5, 5, -10, -20), make_operation_2('-', 5, 5, -10, -20))
print(make_operation_1('*', 7, 6, num3=1, num4=1), make_operation_2('*', 7, 6))