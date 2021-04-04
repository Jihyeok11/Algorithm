import sys
sys.stdin = open("10026in.txt",'r')

n = int(sys.stdin.readline())
li = list(list(x for x in sys.stdin.readline().strip()) for _ in range(n))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
v1 = list(list(True for _ in range(n)) for _ in range(n))
v2 = list(list(True for _ in range(n)) for _ in range(n))
a1 = a2 = 0
for y in range(n):
    for x in range(n):
        if v1[y][x]:
            v1[y][x] = False
            a1 += 1
            c1 = li[y][x]
            b1 = [(y,x)]
            while b1:
                newY,newX = b1.pop()
                for i in range(4):
                    checkY = newY+dy[i]
                    checkX = newX+dx[i]
                    if 0<=checkY<n and 0<=checkX<n and li[checkY][checkX]==c1 and v1[checkY][checkX]:
                        v1[checkY][checkX] = False
                        b1.append((checkY,checkX))
        if v2[y][x]:
            a2 += 1
            c2 = li[y][x]
            b2 = [(y,x)]
            v2[y][x] = False
            while b2:
                newY, newX = b2.pop()
                for i in range(4):
                    checkY = newY+dy[i]
                    checkX = newX+dx[i]
                    if 0<=checkY<n and 0<=checkX<n and v2[checkY][checkX]:
                        if c2=="R" or c2=="G":
                            if li[checkY][checkX]=="R" or li[checkY][checkX]=="G":
                                v2[checkY][checkX] = False
                                b2.append((checkY,checkX))
                        else:
                            if li[checkY][checkX]=="B":
                                v2[checkY][checkX] = False
                                b2.append((checkY,checkX))
print("{} {}".format(a1,a2))