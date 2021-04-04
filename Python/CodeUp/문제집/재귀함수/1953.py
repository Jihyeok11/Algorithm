def star(n):
    
    if n != 1:
        star(n-1)
        print('*'*n)
    else :
        print('*')
    
a = int(input())
star(a)