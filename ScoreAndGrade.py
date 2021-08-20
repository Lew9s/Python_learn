Score = eval(input('Please enter the score:'))
if 0<= Score <= 100:
    if 90 <= Score <= 100:
        grade = 'A'
    elif Score >= 70:
        grade = 'B'
    elif Score >= 60:
        grade = 'C'
    elif Score >= 0:
        grade = 'D'
    print("The grade of {} is {}.".format(Score,grade))
else:
    print('Invalid score')
