from math import *

CONST_RADIUS = 2


try:
    x = float(input('Введите значение х: '))
    if -6 <= x <= -2:
        y = -(x ** 2) - 7*x - 10
    elif 2 < x <= 2:
        y = sqrt(CONST_RADIUS**2 - x ** 2)
    elif 2 < x <= 8:
        y = log(x, 2) - 1
    elif 8 < x:
        y = -2 * x + 18
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
print("x: {} y:{}".format(x, y))