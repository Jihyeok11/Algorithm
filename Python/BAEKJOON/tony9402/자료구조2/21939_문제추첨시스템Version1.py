import sys
sys.stdin = open("23939in.txt", 'r')

li = []
for _ in range(int(sys.stdin.readline().strip())):
    li.append(list(map(int, sys.stdin.readline().strip().split())))
li = sorted(li, key = lambda x : (x[1], x[0]))
for _ in range(int(sys.stdin.readline().strip())):
    