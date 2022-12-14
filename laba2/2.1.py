from math import *
q=0
while q==0:
    z=input('Введите значение x=')
    if z=='закончить':
        break
    try:
        z=float(z)
    except ValueError:
        continue
    if z=='':
        continue
    else:
        x=float(z)
        if x <-6:
            y=0
        elif x>=-6 and x <-2:
            y=-((x+3.5)**2)+2.25
        elif x>=-2 and x<2:
            y=-sqrt(4-x**2)
        elif x>=2 and x<=8:
            y=log2(x)-1
        else:
            y=-x*2+18
        print('X=',x,'Y=',y)