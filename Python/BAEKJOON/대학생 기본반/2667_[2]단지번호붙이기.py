import sys
sys.stdin = open("2667in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = list(list( int(x) for x in sys.stdin.readline().strip()) for _ in range(n))
vi = list(list(True for _ in range(n)) for _ in range(n))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answer = []
for y in range(n):
    for x in range(n):
        if li[y][x] and vi[y][x]:
            cnt = 1
            vi[y][x] = False
            ba = [(y,x)]
            while ba:
                newY,newX = ba.pop()
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0<=checkY<n and 0<=checkX<n and vi[checkY][checkX] and li[checkY][checkX]:
                        ba.append((checkY,checkX))
                        vi[checkY][checkX] = False
                        cnt += 1
            answer.append(cnt)
print(len(answer))
answer.sort()
for i in answer:
    print(i)