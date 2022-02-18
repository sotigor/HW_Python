
def euclidean_gcd(num_1, num_2):
    """ Calculating the greatest common divisor of two integer numbers by euclidean method
    """
    try:
        num_1 = int(num_1)
        num_2 = int(num_2)
    except ValueError:
        return f"Check your entered '{a}' and '{b}' values. \n" \
               "The values should be integer positive numbers."
    else:
        if num_1 > 0 and num_2 > 0:
            while num_1 != num_2:
                if num_1 > num_2:
                    num_1 = num_1 - num_2
                else:
                    num_2 = num_2 - num_1
            return num_1
        else:
            return f"Check your entered '{a}' and '{b}' values. \n" \
               "The values should be integer positive numbers."


a = input("Finding the greatest common divisor of two integer numbers."
          " \nPlease, enter the first number (should be integer positive): ")
b = input("Finding the greatest common divisor of two integer numbers."
          " \nPlease, enter the second number (should be integer positive): ")

print(euclidean_gcd(a, b))
