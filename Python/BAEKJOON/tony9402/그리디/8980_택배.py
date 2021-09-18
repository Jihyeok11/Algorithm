import sys
sys.stdin = open("8980in.txt", 'r')

town, limit_load = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
li = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
li = sorted(li, key = lambda x:x[1])
answer = 0
loads = list(0 for _ in range(town + 1))
for i in range(n):
    a, b, c = li[i]
    load_max = 0
    for j in range(a, b):
        load_max = max(loads[j], load_max)
    result = min(c, limit_load - load_max)
    answer += result
    for j in range(a, b):
        loads[j] += result
print(answer)