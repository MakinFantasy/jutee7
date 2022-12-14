from random import *


def init():
    try:
        n = int(input('Введите кол-во элементов'))
        array = []
        for i in range(n):
            array.append(randint(-10, 10))
        print(array)
        return array
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


def main(array):
    try:
        y = float(input('Введите y: '))
        if not(min(array) < y < max(array)):
            print('Введите корректное по условию значение y')
            exit(1)
        more_arr = []
        for i in array:
            if abs(i) > y:
                more_arr.append(i)
        print(more_arr)
        result = 1
        for i in more_arr:
            result *= i
        print("Произведение = ", result)
        other_arr = []
        for i in array:
            if abs(i) <= y:
                other_arr.append(i)
        print(other_arr)
        result = 0
        for i in other_arr:
            result += i
        print("Сумма = ", result)
    except Exception as e:
        print(e)
        print(e.__doc__)
        exit(1)


arr = init()
main(arr)
