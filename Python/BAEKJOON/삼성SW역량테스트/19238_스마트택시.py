import sys
from collections import deque
sys.stdin = open("19238in.txt",'r')

dy = [-1,0,0,1]
dx = [0,-1,1,0]
def goTaxi(y,x): # 현재위치에서 가장 가까운 곳 찾기
    vi = list(list(True for _ in range(n)) for _ in range(n))
    vi[y][x] = False
    li = deque([(y,x,0)])
    result = [(10**10,10**10,10**10)]
    flag = True
    while li:
        newY,newX,dist = li.popleft()
        if not flag:
            if dist > result[0][2]:
                result = sorted(result, key=lambda x : (x[0],x[1]))
                return result[0][0],result[0][1],result[0][2]
            elif (newY,newX) in people:
                result.append((newY,newX,dist))
            
        if flag and (newY,newX) in people:
            result = [(newY,newX,dist)]
            flag = False
        for i in range(4):
            checkY = newY+dy[i]
            checkX = newX+dx[i]
            if 0<=checkY<n and 0<=checkX<n and not maze[checkY][checkX] and vi[checkY][checkX] :
                vi[checkY][checkX] = False 
                li.append((checkY,checkX,dist+1))
    result = sorted(result, key=lambda x:(x[0],x[1]))
    return result[0][0],result[0][1],result[0][2]

    
def goGoal(y,x,goalY,goalX):
    vi = list(list(True for _ in range(n)) for _ in range(n))
    li = deque([(y,x,0)])
    while li:
        newY,newX,dist = li.popleft()
        if newY== goalY and newX == goalX:
            return dist
        for i in range(4):
            checkY = newY+dy[i]
            checkX = newX+dx[i]
            if 0<=checkY<n and 0<=checkX<n and not maze[checkY][checkX] and vi[checkY][checkX] :
                vi[checkY][checkX] = False
                li.append((checkY,checkX,dist+1))
    return 10**10

n,m,l = map(int,sys.stdin.readline().split())
maze = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))
y,x = map(int,sys.stdin.readline().split())
ba = list(list(map(int,sys.stdin.readline().split())) for _ in range(m))
y -= 1
x -= 1
flag = True
people = []
goal = []
for b in ba:
    people.append((b[0]-1,b[1]-1))
    goal.append((b[2]-1,b[3]-1))
while people:
    A = goTaxi(y,x)
    l -= A[2]
    if l<0:
        print(-1)
        flag = False
        break
    idx = people.index((A[0],A[1]))
    waste = goGoal(people[idx][0],people[idx][1],goal[idx][0],goal[idx][1])
    y = goal[idx][0]
    x = goal[idx][1]
    people.pop(idx)
    goal.pop(idx)
    l -= waste
    if l<0:
        flag = False
        print(-1)
        break
    else:
        l += (2*waste)
if flag:
    print(l)