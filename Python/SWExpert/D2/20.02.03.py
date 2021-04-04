import random


def iswall(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return True
    return False
            

List = []
for i in range(5):
    List.append([])
    for j in range(5):
        List[i].append(0)
        
List_random = []
for i in range(26):
    List_random.append(i)
random.shuffle(List_random)
for i in range(5):
    for j in range(5):
        List[i][j] = List_random[5*i+j]

List = [[14, 6, 7, 21, 3], [24, 4, 16, 9, 11], [15, 18, 2, 12, 17], [19, 1, 8, 13, 0], [25, 20, 23, 5, 22]]
N=5
dx = [0,0,-1,1]
dy = [-1,1,0,0]
total = 0
for y in range(5):
    for x in range(5):
        for i in range(4):
            testX = x+dx[i]
            testY = y+dy[i]
            if iswall(testY,testX)==False:
                tmp = abs(List[testY][testX] - List[y][x])
                total += tmp
print(total)

