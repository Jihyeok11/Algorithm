def one(n):
    if n == 1:
        return 1
    elif n%2:
        one(3*n+1)
        print(3*n+1)
    else :
        one(n//2)
        print(n//2)

n = int(input())
one(n)
print(n)