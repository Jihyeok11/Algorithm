import sys
sys.stdin = open("1463in.txt",'r')

import sys
def one(n,cnt):
    global ans
    if n==1:
        if ans > cnt:
            ans = cnt
        return
    if cnt > ans:
        return
    if not n%3:
        one(n//3,cnt+1)
    if not n%2:
        one(n//2, cnt+1)
    one(n-1,cnt+1)
    
n = int(sys.stdin.readline())
ans = 10000
one(n,0)
print(ans)