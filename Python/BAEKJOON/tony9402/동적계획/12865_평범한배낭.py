import sys
sys.stdin = open("12865in.txt", 'r')

n,k = map(int ,sys.stdin.readline().strip().split())
li = []
for _ in range(n):
    li.append(list(map(int ,sys.stdin.readline().strip().split())))
li = sorted(li, key=lambda x:(-x[1], x[0]))
ba = []
for w, v in li:
    