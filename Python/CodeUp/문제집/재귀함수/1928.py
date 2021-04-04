def one(n):
    if n == 1:
        return 1
    elif n%2:
        print(3*n+1)
        return one(3*n+1)
    else :
        print(n//2)
        return one(n//2)

n = int(input())
print(n)
one(n)