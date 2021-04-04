import sys
sys.stdin = open("1026in.txt",'r')

import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
answer = 0
while a:
    A = a.pop(0)
    Max = idx = 0
    for i in range(n):
        if Max < b[i]:
            Max = b[i]
            idx = i
    b[idx] = 0
    answer += A*Max
print(answer)