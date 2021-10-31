import sys
sys.stdin = open("11053in.txt", 'r')

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().strip().split()))
ba = list(0 for _ in range(n))
for i in range(n-1):
    for j in range(i+1, n):
        if li[i] < li[j]:
            ba[i] += 1
print(ba)
print(max(ba))