import sys, math
sys.stdin = open("2141in.txt", 'r')

n = int(sys.stdin.readline())
town = [] # [(1, 3), (2, 5), (3, 3)]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    town.append((a, b))
idx = 0
Min = math.inf
for i in range(n):
    total = 0
    for j in range(n):
        total += abs(town[i][0] - town[j][0]) * town[j][1]
    if total < Min:
        Min = total
        idx = town[i][0]
print(idx)