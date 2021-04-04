import sys
sys.stdin = open("17626in.txt",'r')

import sys
def rangzhu(num,cnt):
    global ans
    if cnt>4:
        return
    if not num:
        if ans > cnt:
            ans = cnt
        return True
    for i in range(int(num**0.5),0,-1):
        if i*i > num-i*i:
            rangzhu(num-i*i,cnt+1)

n = int(sys.stdin.readline())
ans = 1000
rangzhu(n,0)
print(ans)