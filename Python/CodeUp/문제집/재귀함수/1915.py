def Pibo(n):
    if n == 1 : 
        return 1
    elif n == 2:
        return 1
    else:
        return Pibo(n-2) + Pibo(n-1)

N = int(input())
print(Pibo(N))
