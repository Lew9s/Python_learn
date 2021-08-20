from math import sqrt
a, b, c=eval(input())
t = b*b-4*a*c
if t > 0:
    x1=(-b+sqrt(t))/2*a
    x2=(-b-sqrt(t))/2*a
    print('x1 = {:.1f}, x2 = {:.1f}'.format(x1,x2))
elif t == 0:
    x = -b/(2*a)
    print('x = {:.1f}'.format(x))
else:
    print("no real solution.")
