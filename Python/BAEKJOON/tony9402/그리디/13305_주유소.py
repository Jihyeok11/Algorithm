import sys
sys.stdin = open("13305in.txt", 'r')

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().strip().split()))
t = list(map(int,sys.stdin.readline().strip().split()))
fee = 10**10
toll = 0
for i in range(len(l)):
    fee = min(fee, t[i])
    toll += fee * l[i]
print(toll)