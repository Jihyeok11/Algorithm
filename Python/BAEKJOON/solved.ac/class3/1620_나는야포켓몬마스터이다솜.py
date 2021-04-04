import sys
sys.stdin = open("1620in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
li = []
pocket = {}
for i in range(n):
    mon = sys.stdin.readline().strip()
    li.append(mon)
    pocket[mon] = i+1
for _ in range(m):
    a = sys.stdin.readline().strip()
    if a.isdigit():
        print(li[int(a)-1])
    else:
        print(pocket[a])