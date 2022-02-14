import sys
from collections import defaultdict
sys.stdin = open("2606in.txt", 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
computers = defaultdict(list)
for _ in range(m):
    a, b = map(int ,sys.stdin.readline().split())
    computers[a].append(b)
    computers[b].append(a)
virus_list = [1]
visited_virus = list(True for _ in range(n+1))
answer = 0
while virus_list:
    check = virus_list.pop()
    if visited_virus[check]:
        visited_virus[check] = False
        answer += 1
        for i in computers[check]:
            if visited_virus[i] and not i in virus_list:
                virus_list.append(i)
print(answer)