import sys
sys.stdin = open("2636in.txt",'r')

from copy import deepcopy

def iswall(y,x):
    if y>=Y or x >= X or x<0 or y<0:
        return True
    return False

def Count(y,x):
    global Dict
    dy = [0,0,-1,1]
    dx = [-1,1,0,0]
    for i in range(4):
        c_y = y+dy[i]
        c_x = x+dx[i]
        if iswall(c_y,c_x)==False:
            if List[c_y][c_x]==0:
                if not (c_y,c_x) in Dict:
                    Dict.append((c_y,c_x)) 
                    Count(c_y,c_x)



Y,X = map(int,input().split())
List = [ list(map(int,input().split())) for _ in range(Y)]
C_L = deepcopy(List)
Answer = 0
while True:
    Answer += 1
    Dict = []
    A = 0
    y = 0
    while y != Y:
        for x in range(X):
            if List[y][x]==0:
                Count(y,x)
                y = Y
                break
            

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    for i in range(len(Dict)):
        y = Dict[i][0]
        x = Dict[i][1]
        for _ in range(4):
            C_Y = y+dy[_]
            C_X = x+dx[_]
            if iswall(C_Y,C_X)==False: 
                A = 1
                List[C_Y][C_X] = 0
    
    if A == 0:
        break
    count = total
    
print(Answer)
print(count)
    