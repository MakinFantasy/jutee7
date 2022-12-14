from random import uniform

try:
    R = float(input('Введите радиус: '))
    print(" " * 5 + "X" + " " * 10 + "Y" + " " * 7 + "Res" + " " * 5)
    print("-" * 32)
    for i in range(10):
        X = uniform(-2 * R, 2 * R)
        Y = uniform(-2 * R, 2 * R)
        try:
            if ((-R <= X <= 0) and (-R <= Y <= 0) and (Y >= -X - R)) \
                    or ((R ** 2 >= X ** 2 + Y ** 2) and (0 <= X <= R) and (0 <= Y <= R)):
                print("{0: 10.2f}{1: 10.2f}".format(X, Y) + "\tTrue")
            else:
                print("{0: 10.2f}{1: 10.2f}".format(X, Y) + "\tFalse")
        except Exception as e:
            print(e)
            print(e.__doc__)
            exit(1)
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
