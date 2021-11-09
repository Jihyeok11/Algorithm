import sys
from collections import deque, defaultdict
sys.stdin = open("22864in.txt",'r')

A, B, C, M = map(int, sys.stdin.readline().split())
ba = deque([(0, 0)])
answer = 0
clocks = defaultdict(int)
for _ in range(24):
    for i in range(len(ba)):
        a, b = ba.popleft()
        if answer < b:
            answer = b
        if a + A <= M and clocks[a+A] < b+B:
            clocks[a+A] = B
            ba.append((a+A, b+B))
        ba.append((max(a-C, 0), b))
print(ba)
print(answer)