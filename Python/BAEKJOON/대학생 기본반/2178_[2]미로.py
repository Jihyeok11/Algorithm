import sys
sys.stdin = open("2178in.txt",'r')

from collections import deque
import sys
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n,m = map(int,sys.stdin.readline().split())
ba = deque([(0,0,0)])
li = list(list( int(x) for x in sys.stdin.readline().strip()) for _ in range(n))
print(li)
vi = list(list(True for _ in range(m)) for _ in range(n))
while ba:
    newY,newX,cnt = ba.popleft()
    if newY==n-1 and newX == m-1:
        print(cnt+1)
        break
    for i in range(4):
        checkY = newY + dy[i]
        checkX = newX + dx[i]
        if 0<= checkY < n and 0<=checkX < m and li[checkY][checkX] and vi[checkY][checkX]:
            vi[checkY][checkX] = False
            ba.append((checkY,checkX,cnt+1))