import sys
sys.stdin = open("2285in.txt", 'r')

n = int(sys.stdin.readline())
li = list(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
li.sort()
pp = 0
for i in range(n):
    pp += li[i][1]
cnt = idx = 0
while True:
    cnt += li[idx][1]
    if cnt >= pp / 2:
        print(li[idx][0])
        break
    idx += 1