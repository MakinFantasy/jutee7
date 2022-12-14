from math import sin, cos, tan


print('Первая формула')
for i in range(5):
    try:
        a = float(input('Enter a: '))
        try:
            z = (sin(a) ** 2 - tan(a) ** 2) / (cos(a) ** 2 - (1 / tan(a)) ** 2)
            print('Ответ: ', z)
        except Exception as e:
            print('ОДЗ')
    except Exception as e:
        exit('Введен неверное значение а')


print('Вторая формула')
for i in range(5):
    try:
        a = float(input('Enter a: '))
        try:
            z = tan(a)**6
            print('Ответ: ', z)
        except Exception as e:
            print('ОДЗ')
    except Exception as e:
        exit('Введен неверное значение а')
