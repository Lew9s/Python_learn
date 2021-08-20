x = eval(input('Enter a number:'))
if x != 0:
    if x < 0:
        sgn = -1
    else:
        sgn = 1
else:
    sgn = 0
print('sgn = {:.0f}'.format(sgn))

