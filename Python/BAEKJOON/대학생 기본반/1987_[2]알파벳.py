import sys
sys.stdin = open("1987in.txt",'r')

import sys
Y,X = map(int,sys.stdin.readline().split())
li = list(list(x for x in sys.stdin.readline().strip()) for _ in range(Y))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
Max = 0
    
def myAlpha(y,x,leng):
    global Max, vi
    if leng > Max:
        Max = leng
    for i in range(4):
        checkY = y + dy[i]
        checkX = x + dx[i]
        if 0<= checkY < Y and 0<= checkX < X and vi[ord(li[checkY][checkX])-65]:
            vi[ord(li[checkY][checkX])-65] = False
            myAlpha(checkY,checkX,leng+1)
            vi[ord(li[checkY][checkX])-65] = True

ba = [(0,0,1)]
vi = [True]*26
vi[ord(li[0][0])-65] = False
myAlpha(0,0,1)
print(Max)