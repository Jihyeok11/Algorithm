import sys
sys.stdin = open("11724in.txt",'r')

import sys
N,K = map(int,sys.stdin.readline().split())
basket = {}
for i in range(N+1):
    basket[i] = []
for _ in range(K):
    A,B = map(int,sys.stdin.readline().split())
    basket[A].append(B)
    basket[B].append(A)
visited = list(True for _ in range(N+1))
answer = 0
for i in range(1,N+1): 
    if visited[i]:
        visited[i] = False
        answer += 1
        l=[]
        for j in basket[i]:
            if visited[j]:
                visited[j] = False
                l.append(j)
        while l:
            k = l.pop()
            for m in basket[k]:
                if visited[m]:
                    visited[m] = False
                    l.append(m)
print(answer)