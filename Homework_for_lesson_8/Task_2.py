
def nested_parentheses(incoming):
    """Функція контролює коректність використання дужок ( )

    Виявляє відсутність відповідної дужки до вже існуючої,
    а також виявляє помилки виду: )( , коли дужки неправильно розвернуті.
    Обробляє зокрема математичні вирази.
    """
    lst_incoming = list(incoming)
    if lst_incoming.count('(') == lst_incoming.count(')'):
        if lst_incoming.count('(') > 0:
            counter = lst_incoming.count('(')
            while counter > 0:
                if lst_incoming.index('(') < lst_incoming.index(')'):
                    lst_incoming.pop(lst_incoming.index('('))
                    lst_incoming.pop(lst_incoming.index(')'))
                else:
                    return False
                counter -= 1
            else:
                return True
        else:
            return True
    else:
        return False

print(nested_parentheses("((())(())())"))
print(nested_parentheses(""))
print(nested_parentheses("(((())))"))
print(nested_parentheses("())"))
print(nested_parentheses("(()()(())"))
print(nested_parentheses('1+2+4(5+7)*64(-1)(3+4)((+2)'))
print(nested_parentheses('1+2+4-(5+7)*64(-1)(3+4)(+2)'))




