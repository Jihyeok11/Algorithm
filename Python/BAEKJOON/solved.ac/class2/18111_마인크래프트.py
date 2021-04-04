import sys
sys.stdin = open("18111in.txt",'r')

import sys

n,m,b = map(int,sys.stdin.readline().split())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
minTime = 1000000000000000000000000000000
ans = 0
for height in range(257):
    bag = b
    time = 0
    for y in range(n):
        for x in range(m):
            if li[y][x] > height:
                bag += (li[y][x]-height)
                time += ( 2* (li[y][x]-height))
            else:
                time += (height-li[y][x])
                bag -= (height-li[y][x])
    if bag < 0:
        continue
    if time <= minTime:
        minTime = time
        ans = height
print(minTime,ans)