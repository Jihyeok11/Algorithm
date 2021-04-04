def jaegui(n):
    if n == 1:
        print(1)
    else:
        print(n)
        jaegui(n-1)

a = int(input())
jaegui(a)