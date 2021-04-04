import sys
sys.stdin = open("1929in.txt",'r')

import sys
def mydec(b):
    global vi
    for i in range(2,int(b**0.5)+1):
        if vi[i]:
            for j in range(2*i,b+1,i):
                vi[j] = False

m,n = map(int,sys.stdin.readline().split())
vi = [True]*(n+1)
vi[1] = False
mydec(n)
for i in range(m,n+1):
    if vi[i]:
        print(i)