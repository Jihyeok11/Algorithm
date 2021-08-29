import sys
sys.stdin = open("1092in.txt", 'r')

n = int(sys.stdin.readline())
container = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)
m = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)

if boxes[0] > container[0]:
    print(-1)
else:
    locations = []
    cnt = 0
    idx = 0
    for c in range(n):
        while boxes[idx] > container[c] and idx < m:
            idx += 1
        if idx < m:
            locations.append(idx)
    res = []
    for i in
    print(locations)