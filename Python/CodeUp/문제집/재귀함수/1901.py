def jaegui(n):
    if n == 1:
        print(1)
    else:
        jaegui(n-1)
        print(n)
a = int(input())
jaegui(a)