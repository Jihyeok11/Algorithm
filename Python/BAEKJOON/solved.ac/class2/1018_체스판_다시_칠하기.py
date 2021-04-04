import sys
sys.stdin = open("1018in.txt",'r')

import sys
m,n = map(int,sys.stdin.readline().split())
li = list( list( x for x in sys.stdin.readline().strip()) for _ in range(n))
def check_w(checkY,checkX):
    global result
    miss = 0
    for y in range(8):
        for x in range(8):
            if li[checkY+y][checkX+x] == "B" and (checkY+y+checkX+x)%2:
                miss += 1
            elif li[checkY+y][checkX+x] == "W" and (not (checkY+checkX+y+x)%2):
                miss += 1
            if miss > result:
                return
    else:
        result = miss

def check_b(checkY,checkX):
    global result
    miss = 0
    for y in range(8):
        for x in range(8):
            if li[checkY+y][checkX+x] == "W" and (checkY+y+checkX+x)%2:
                miss += 1
            elif li[checkY+y][checkX+x] == "B" and (not (checkY+checkX+y+x)%2):
                miss += 1
            if miss > result:
                return
    else:
        result = miss



result = 10**10
for y in range(m-7):
    for x in range(n-7):
        check_b(y,x)
        check_w(y,x)
print(result)