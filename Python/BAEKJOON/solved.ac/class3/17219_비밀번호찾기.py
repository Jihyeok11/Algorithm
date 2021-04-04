import sys
sys.stdin = open("17219in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
page = {}
for _ in range(n):
    a,b = sys.stdin.readline().split()
    page[a] = b
for _ in range(m):
    a = sys.stdin.readline().strip()
    print(page[a])