import sys
sys.stdin = open("2581in.txt", 'r')

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ba = []
vi = list(True for _ in range(10001))
vi[1] = False
for i in range(2,int(m**(1/2))+1):
    for j in range(2*i, 10001, i):
        if vi[j]:
            vi[j] = False
for i in range(n, m+1):
    if vi[i]:
        ba.append(i)
if ba:
    print(sum(ba))
    print(ba[0])
else:
    print(-1)