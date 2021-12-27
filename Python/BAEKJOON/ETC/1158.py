import sys
sys.stdin = open("1158in.txt", 'r')

n,m = map(int,input().split())
li = list(range(1, n+1))
answer = []
loc = 0
for _ in range(n):
    loc += m-1
    if loc >= len(li):
        loc %= len(li)
    answer.append(li.pop(loc))
print("<" + ", ".join(map(str, answer)) + ">")