import sys
sys.stdin = open("2606in.txt",'r')

import sys
n = int(sys.stdin.readline())
l = int(sys.stdin.readline())
computers = {}
for i in range(1,n+1):
    computers[i] = []
for _ in range(l):
    A,B = map(int,sys.stdin.readline().split())
    computers[A].append(B)
    computers[B].append(A)
visited = [True]*(n+1)
visited[1] = False
basket = computers[1]
answer = 0
for i in computers[1]:
    answer += 1
    visited[i] = False
while basket:
    check = basket.pop()
    for i in computers[check]:
        if visited[i]:
            visited[i]=False
            answer += 1
            basket.append(i)
print(answer)