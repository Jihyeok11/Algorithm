Str = ''
def half(n):
    global Str
    if n<2:
        Str += str(n%2)
        return Str 
    else:
        Str += str(n%2)
        return half(n//2)
    
N = int(input())
print(half(N)[::-1])


#10 = 1010