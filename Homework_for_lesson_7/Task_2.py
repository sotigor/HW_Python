# Creating a function which returns the total price of stock.

# Provided two dictionaries

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# First method. Using dictionary comprehension.
element_prices = {key_s: stock[key_s] * prices[key_p] for (key_s, value_s) in stock.items()
                  for (key_p, value_p) in prices.items() if key_s == key_p}
total_price = sum(element_prices.values())
print(f'The total price of stock is: {total_price}')


# Second method. Using function.
def total_stock_price(dict_1, dict_2):
    """Calculating the total price of stock"""
    sum_of_prices = 0
    for item in dict_1:
        sum_of_prices += dict_1[item]*dict_2[item]
    return sum_of_prices


print(f'The total price of stock is: {total_stock_price(stock,prices)}')
