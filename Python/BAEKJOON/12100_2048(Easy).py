import sys
sys.stdin = open("12100in.txt",'r')

import sys,copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def mymaze(mylist,cnt):
    global ans
    if cnt>=5:
        Max = max(map(max, mylist))
        if ans < Max:
            ans = Max
        return
    for i in range(4):
        newList = copy.deepcopy(mylist)
        vi = list(list(True for _ in range(n)) for _ in range(n))
        if i==0 or i==2:
            for y in range(n):
                for x in range(n):
                    if newList[y][x]:
                        checkY,checkX = y+dy[i],x+dx[i]
                        while 0 <= checkY < n and 0 <= checkX < n and (not newList[checkY][checkX]):
                            checkY += dy[i]
                            checkX += dx[i]
                        if 0<= checkY<n and 0<=checkX<n:
                            if (checkY != y or checkX != x) and newList[y][x] == newList[checkY][checkX]:
                                if vi[checkY][checkX]:
                                    pass
                                else:
                                    pass
                                
n = int(sys.stdin.readline())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
ans = 0