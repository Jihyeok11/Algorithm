import sys
sys.stdin = open("1620in.txt",'r')

n, m = map(int,sys.stdin.readline().strip().split())
li = list(sys.stdin.readline().strip() for _ in range(n))
ba = {}
for i in range(n):
    ba[li[i]] = i + 1
for _ in range(m):
    a = sys.stdin.readline().strip()
    if a.isalpha():
        print(ba[a])
    else:
        print(li[int(a) - 1])