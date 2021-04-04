import sys
sys.stdin = open("18870in.txt",'r')

n = int(sys.stdin.readline())
li = list( map(int,sys.stdin.readline().split()))
st = sorted(set(li))
st = { st[i]:i for i in range(len(st)) }
print(*[ st[x] for x in li])
































# n=int(input())
# x=list(map(int,input().split()))
# xt=list(sorted(set(x)))
# xt={xt[i]:i for i in range(len(xt))}
# print(*[xt[i] for i in x])