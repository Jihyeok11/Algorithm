import sys
sys.stdin = open("2775in.txt",'r')


# 1층 3호, 2층 3호
import sys
li = [[1]]
def strech_list(a,b):
    # a 는 2, b는 3
    global li
    while len(li) <= a:
        li.append([1])
    for i in range(a+1):
        while len(li[i]) < b:
            li[i].append(0)

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    strech_list(k,n)
    for x in range(n):
        if not li[0][x]:
            li[0][x] = x+1
    for y in range(k+1):
        for x in range(n):
            if not li[y][x]:
                li[y][x] = li[y-1][x] + li[y][x-1]
    print(li[k][n-1])