import sys
sys.stdin = open("2589in.txt",'r')

import sys
from collections import deque
Y,X = map(int,sys.stdin.readline().split())
tre = list(list(x for x in sys.stdin.readline().strip()) for _ in range(Y))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answer = 0
def checkIfCorner(arr, x, y):
    if (0 <= x + 1 < len(arr) and arr[x + 1][y] == 'L') and (0 <= x - 1 < len(arr) and arr[x - 1][y] == 'L'):
        return False
    if (0 <= y + 1 < len(arr[0]) and arr[x][y + 1] == 'L') and (0 <= y - 1 < len(arr[0]) and arr[x][y - 1] == 'L'):
        return False
    return True
    
for y in range(Y):
    for x in range(X):
        if tre[y][x]=="L":
            vi = list(list(1 for _ in range(X)) for _ in range(Y))
            vi[y][x] = 0
            ba = deque([(y,x,0)])
            result = 0
            while ba:
                newY,newX,cnt = ba.popleft()
                result = max(result,cnt)
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0<= checkY<Y and 0<=checkX<X and vi[checkY][checkX] and tre[checkY][checkX]=="L":
                        vi[checkY][checkX] = 0
                        ba.append((checkY,checkX,cnt+1))
            answer = max(result,answer)
print(answer)