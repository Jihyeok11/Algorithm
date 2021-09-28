import sys
sys.stdin = open("15724in.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
li = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
ba = list(list(0 for _ in range(m+1)) for _ in range(n+1))
for y in range(1, n+1):
    for x in range(1, m+1):
        ba[y][x] = ba[y-1][x] + ba[y][x-1] + li[y-1][x-1] - ba[y-1][x-1]
for _ in range(int(sys.stdin.readline())):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(ba[y2][x2] - ba[y2][x1-1] - ba[y1-1][x2] + ba[y1-1][x1-1])
