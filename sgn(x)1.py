x = eval(input('Enter a number:'))
if x < 0:
    sgn = -1
elif x == 0:
    sgn = 0
else:
    sgn = 1
print('sgn = {:.0f}'.format(sgn))
