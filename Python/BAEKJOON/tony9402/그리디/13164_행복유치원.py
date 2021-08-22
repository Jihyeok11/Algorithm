import sys
sys.stdin = open("13164in.txt", 'r')

n, k = map(int, sys.stdin.readline().split())
li = sorted(list(map(int ,sys.stdin.readline().split())), key= lambda x:x)
print(li)
team = []
for i in li:
    if len(team) < k:
        team.append((i, i))
print(team)