import sys
sys.stdin = open("1016in.txt",'r')

import sys
def my_sqrt(a,b):
    for i in range(2,int(b**0.5)+1):
        n = i**2-a%(i**2)
        if n==i**2:
            n=0
        while n <= (b-a):
            if vi[n]:
                vi[n] = False
            n += i**2

a,b = map(int,sys.stdin.readline().split())
vi = [True]*(b-a+1)
my_sqrt(a,b)
ans = 0
for i in vi:
    if i:
        ans += 1
print(ans)