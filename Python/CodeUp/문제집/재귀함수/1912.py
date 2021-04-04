total = 1
def Pac(n):
    global total
    if n == 1:
        return print(total)
    else:
        total *= n
        Pac(n-1)
a = int(input())
Pac(a)