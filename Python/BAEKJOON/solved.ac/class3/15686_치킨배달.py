import sys
sys.stdin = open("15686in.txt",'r')

import sys
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def checkrange():
    chickenrange = [5000]*len(houses)
    for i in range(len(vis)):
        if not vis[i]:
            y,x = stores[i]
            for j in range(len(houses)):
                chickenrange[j] = min(chickenrange[j],abs(houses[j][0]-y)+abs(houses[j][1]-x))      
    return sum(chickenrange)
def check_stores(idx,c):
    global ans
    if c==m:
        res = checkrange()
        if ans > res:
            ans = res
        return
    for i in range(idx,len(stores)):
        if vis[i]:
            vis[i] = False
            check_stores(i+1,c+1)
            vis[i] = True

n,m = map(int,sys.stdin.readline().split())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
stores = []
houses = []
for y in range(n):
    for x in range(n):
        if li[y][x] == 2:
            stores.append((y,x))
        elif li[y][x]:
            houses.append((y,x))
vis = [True]*len(stores)
ans = 1000000
check_stores(0,0)
print(ans)