def f2(n):
    if n >=2:
        f2(n//2)
    print(n%2,end = '')
f2(8)
    
