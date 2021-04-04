import sys
sys.stdin = open("19238in.txt",'r')

from collections import deque

def checkDistance(startY,startX,desY,desX):
    basket = deque([(startY,startX,0)])
    visited = list(list(True for _ in range(N)) for _ in range(N))
    visited[startY][startX] = False
    while basket:
        newY, newX, cnt = basket.popleft()
        if newY == desY and newX == desX:
            return cnt
        for l in range(4):
            pointY = newY + dy[l]
            pointX = newX + dx[l]
            if 0<= pointY < N and 0 <= pointX < N and visited[pointY][pointX] and not List[pointY][pointX]:
                visited[pointY][pointX] = False
                basket.append((pointY,pointX,cnt+1))


def gotoPerson(startY,startX):
    locY = locX = 0
    Min = 1000000
    for i in range(len(person)):
        desY,desX = person[i][0], person[i][1]
        distance = checkDistance(startY,startX,desY,desX)
        if distance == None:
            distance = 1000000
        if Min > distance:
            Min = distance
            locY = person[i][0]
            locX = person[i][1]
            locPerson = i
        elif Min == distance and locY > person[i][0]:
            locY = person[i][0]
            locX = person[i][1]
            locPerson = i
        elif Min == distance and locY == person[i][0] and locX > person[i][1]:
            locY = person[i][0]
            locX = person[i][1]
            locPerson = i
    if Min == 1000000:
        return 2*N, Min
    return locPerson,Min

def checkFuel(startY,startX):
    global fuel
    count = len(person)
    while count:
        target,dist = gotoPerson(startY,startX)
        if target == 2*N:
            return -1
        else:
            if fuel < dist:
                return -1
            fuel -= dist
            locY,locX = person.pop(target)
            goalY,goalX = destination.pop(target)
            check = checkDistance(locY,locX,goalY,goalX)
            if fuel < check:
                return -1
            fuel += check
            count -= 1
            startY,startX = goalY,goalX
    return fuel

dy = [-1,1,0,0]
dx = [0,0,-1,1]
N,M,fuel = map(int,input().split())
List = list(list(map(int,input().split())) for _ in range(N))
startY,startX = map(int,input().split())
startY -= 1
startX -= 1
person = []
destination = []
for i in range(M):
    A,B,C,D = map(int,input().split())
    person.append((A-1,B-1))
    destination.append((C-1,D-1))

print(checkFuel(startY,startX))

    

