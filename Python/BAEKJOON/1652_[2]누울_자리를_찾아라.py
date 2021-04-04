import sys
sys.stdin = open("1652in.txt",'r')

n = int(sys.stdin.readline())
myList = list(list(x for x in sys.stdin.readline().strip()) for _ in range(n))
visitedHorizon = list(list(True for _ in range(n)) for _ in range(n))
visitedVertical = list(list(True for _ in range(n)) for _ in range(n))
horizon = vertical = 0
for y in range(n):
    for x in range(n-1):
        if visitedHorizon[y][x] and myList[y][x] == "." and myList[y][x+1]==".":
            horizon += 1
            Y=y;X=x
            while True:
                try:
                    if myList[Y][X] == ".":
                        visitedHorizon[Y][X] = False
                        X += 1
                    else:
                        break
                except:
                    break
for y in range(n-1):
    for x in range(n):
        if visitedVertical[y][x] and myList[y][x] == "." and myList[y+1][x]==".":
            vertical += 1
            Y=y;X=x
            while True:
                try:
                    if myList[Y][X] == ".":
                        visitedVertical[Y][X] = False
                        Y += 1
                    else:
                        break
                except:
                    break
print("{} {}".format(horizon,vertical))