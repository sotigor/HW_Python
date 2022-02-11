black = float(input('Введите значение для black от 0.00 до 1.00: '))
cyan = float(input('Введите значение для cyan от 0.00 до 1.00: '))
magenta = float(input('Введите значение для magenta от 0.00 до 1.00: '))
yellow = float(input('Введите значение для yellow от 0.00 до 1.00: '))


black = 0
white = (1 - black)
red = 255 * white * (1 - cyan)
green = 255 * white * (1 - magenta)
blue = 255 * white * (1 - yellow)