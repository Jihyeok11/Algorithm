import sys
sys.stdin = open("1629in.txt",'r')

a,b,c = map(int,sys.stdin.readline().split())
def ans(a,b):
    if not b:
        return 1
    elif b==1:
        return a
    elif b%2: 
        return ans(a,b-1)*a %c
    else:
        res = ans(a,b//2)
        return (res**2) %c # 시간을 빠르게 하기 위해서

print(ans(a,b)%c)