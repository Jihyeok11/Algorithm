import sys
sys.stdin = open("1043in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split()) #n은 사람 수, m은 파티 수
li = list(map(int,sys.stdin.readline().split()))
vi = [True]*m
party = []
if li[0]:
    li = set(li[1:])
else:
    li = set(li[1:])
for i in range(m):
    a = list(map(int,sys.stdin.readline().split()))
    if a[0]:
        a = set(a[1:])
        party.append((a,i))
    else:
        vi[i] = False
while True:
    flag = 1
    for i in range(len(party)):
        if li and vi[party[i][1]]:
            if li&party[i][0] and li|party[i][0] == li: # li에 있던 것들만 들어올 때
                li = li|party[i][0]
                vi[i] = False
            elif li&party[i][0]: # 새로운 것이 들어왔을 때
                flag = 0
                vi[i] = False
                li = li|party[i][0]
                break

    if flag:
        break
ans = 0
for i in vi:
    if i:
        ans += 1
print(ans)

    