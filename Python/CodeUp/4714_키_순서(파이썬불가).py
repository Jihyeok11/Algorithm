# 6
# 6
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2

import sys
sys.stdin = open("in.txt",'r')

sys.setrecursionlimit(100000)

def hab(start,N): # 1 , 5
    for i in basket[N]:
        if not i in basket[start]:
            basket[start].append(i)
            hab(start,i)
def rehab(start,N): # 1 , 5
    for i in rebasket[N]:
        if not i in rebasket[start]:
            rebasket[start].append(i)
            rehab(start,i)

st = input().split()
if len(st)>=2:
    students = int(st[0])
    bridge = int(st[1])
else:
    students = int(st[0])
    bridge = int(input())
basket = {} # {1: [5], 2: [], 3: [4], 4: [2, 6], 5: [4, 2], 6: []}
rebasket = {}
for i in range(students):
    basket[i+1] = []
    rebasket[i+1] = []
for _ in range(bridge):
    A,B = map(int,input().split())
    basket[A].append(B)
    rebasket[B].append(A)
for i in range(1,students+1):
    for j in basket[i]:
        hab(i,j)
    for k in rebasket[i]:
        rehab(i,k)
answer = 0
for i in range(1,students+1):
    if len(basket[i]) + len(rebasket[i]) == students-1:
        answer += 1
print(answer)