import sys
sys.stdin = open("1978in.txt",'r')

import sys

def myDec(n):
    global vi
    for i in range(2,int(n**0.5)+1):
        if vi[i]:
            for j in range(2*i,n+1,i):
                vi[j] = False

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
maxNum = max(li)
vi = [True]*(maxNum+1)
vi[1] = False
ans = 0
myDec(maxNum)
for i in li:
    if vi[i]:
        ans += 1
print(ans)