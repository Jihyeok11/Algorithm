import sys
sys.stdin = open("1149in.txt",'r')

import sys

n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
for i in range(1,n):
    li[i][0] = li[i][0] + min(li[i-1][1],li[i-1][2])
    li[i][1] = li[i][1] + min(li[i-1][0],li[i-1][2])
    li[i][2] = li[i][2] + min(li[i-1][1],li[i-1][0])
print(min(li[-1]))