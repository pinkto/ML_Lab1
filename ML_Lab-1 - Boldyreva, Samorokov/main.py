# Написать функцию на вход, которой подается строка.
# Функция должна вернуть true, если каждый символ в строке встречается только 1 раз, иначе должна вернуть false.


def ifTheStrinfTrue():
    string = input('Введите строку: ')
    symb = []
    repeat_symb = []
    for i in string:
        if (i in symb) and (i not in repeat_symb):
            repeat_symb.append(i)
        symb.append(i)
    if len(repeat_symb) > 0:
        print("false")
    else:
        print("true")


ifTheStrinfTrue()
