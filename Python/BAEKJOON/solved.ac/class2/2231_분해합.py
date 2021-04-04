import sys
sys.stdin = open("2231in.txt",'r')

import sys
n = int(sys.stdin.readline())
def check(a,b):
    res = a
    for i in str(a):
        res += int(i)
    if res == b:
        return True
    return False
last = 0
for i in range(n,0,-1):
    if check(i,n):
        last = i
print(last)