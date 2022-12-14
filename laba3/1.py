from math import *


CONST_RADIUS = 2
try:
    start = float(input('Введите стартовую точку: '))
    end = float(input('Введите конечную точку: '))
    dx = float(input('Введите шаг: '))
    if start > end or dx < 0:
        print('Введите правильные аргументы')
        exit(1)

    try:
        print("+" + "-" * 8 + "+" + "-" * 8 + "+")
        print('I   X    I    Y   I')
        print("+" + "-" * 8 + "+" + "-" * 8 + "+")
        print('Xbeg= ' + str(start) + " Xend= " + str(end) + '\n' + '  Dx=  ' + str(dx))
        while start <= end:
            if -6 <= start <= -2:
                y = -(start ** 2) - 7 * start - 10
            elif 2 < start <= 2:
                y = sqrt(CONST_RADIUS ** 2 - start ** 2)
            elif 2 < start <= 8:
                y = log(start, 2) - 1
            elif 8 < start:
                y = -2 * start + 18
            print("I{0: 7.2f} I{1: 7.2f} I".format(start, y))
            start += dx
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)


