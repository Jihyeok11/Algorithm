import sys
sys.stdin = open("22864in.txt",'r')

A, B, C, M = map(int, sys.stdin.readline().split())
p = w = 0
for cnt in range(24):
    if p + A <= M:
        w += B
        p += A
    else:
        p = max(0, p-C)
print(w)