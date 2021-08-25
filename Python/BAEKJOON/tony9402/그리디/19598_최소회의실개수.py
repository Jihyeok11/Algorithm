import sys
sys.stdin = open("19598in.txt", 'r')

n = int(sys.stdin.readline())
li = []
for i in range(n):
    a, b = int(sys.stdin.readline().strip().split())
    li.append((a, 1))
    li.append((b, -1))
r = 0
for _, a in li:
    r += a
    