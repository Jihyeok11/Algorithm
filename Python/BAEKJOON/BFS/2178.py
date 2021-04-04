import sys
sys.stdin = open("2178in.txt",'r')

lenY,lenX = map(int,input().split())
List = [[int(x) for x in input()] for _ in range(lenY) ]

dy=[0,0,-1,1]
dx=[-1,1,0,0]

Direction =[(0,0)]

cnt = 0

while Direction:
    cnt += 1
    Road = [] # 새로운 추가 구역들
    while Direction: # 기존의 추가들 구역들
        Y,X = Direction.pop(0)
        List[Y][X] = str(cnt)
        for i in range(4):
            C_Y = Y+dy[i]
            C_X = X+dx[i]
            if 0<=C_Y<lenY and 0<=C_X<lenX and List[C_Y][C_X]==1:
                Road.append((C_Y,C_X))
    Direction = Road[:]
    

print(int(cnt))


