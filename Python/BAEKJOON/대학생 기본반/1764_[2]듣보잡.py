import sys
sys.stdin = open("1764in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
li1=set()
li2=set()
for _ in range(n):
    li1.add(sys.stdin.readline().strip())
for _ in range(n):
    li2.add(sys.stdin.readline().strip())
se = list(li1&li2)
se.sort()
print(len(se))
for i in se:
    print(i)