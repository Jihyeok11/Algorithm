import sys
sys.setrecursionlimit(100000)


total = 0
def jaegui(n):
    global total
    if n == 1:
        total +=1
    else:
        total += n
        jaegui(n-1)
    return 
    
a = int(input())
jaegui(a)
print(total)