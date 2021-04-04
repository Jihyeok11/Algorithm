import sys
sys.stdin = open("11050in.txt",'r')

n,k = map(int,sys.stdin.readline().split()) # 5,2
ans = 1
cnt = 0
while cnt<k:
    ans *= ((n-cnt) / (cnt+1))
    cnt += 1
print(int(ans))