try:
    R = float(input("Enter radius: "))
    X = float(input("Enter X: "))
    Y = float(input("Enter Y: "))
except Exception as e:
    print(e.__doc__)
    exit(1)

try:
    if ((-R <= X <= 0) and (-R <= Y <= 0) and (Y >= -X - R)) \
            or ((R**2 >= X**2 + Y ** 2) and (0 <= X <= R) and (0 <= Y <= R)):
        print("Попал")
    else:
        print("Не попал")
except Exception as e:
    print(e)
    print(e.__doc__)
    exit(1)
