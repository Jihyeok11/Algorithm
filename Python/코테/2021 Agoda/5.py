import sys
sys.stdin = open("5in.txt",'r')

n = int(input())
ba = {} # {1: [2], 2: [1, 3, 4], 3: [2, 4], 4: [2, 3]}
for _ in range(n):
    l, r = input().split(": ")
    rs = list(map(int,r.split(", ")))
    ba[int(l)] = []
    for i in rs:
        ba[int(l)].append(i)
for i in ba:
    va = [i]
    