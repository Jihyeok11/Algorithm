import sys
sys.setrecursionlimit(100000)

Dict = {}
def stair(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    elif n in Dict:
        return Dict[n]
    else :
        Dict[n] = stair(n-1)+stair(n-2)+stair(n-3)
        return Dict[n]

a = int(input())
print(stair(a)%1000)