import sys
sys.stdin = open('1158in.txt','r')

n,m = map(int,sys.stdin.readline().split())
answer="<"
vi = list(True for _ in range(n))
cnt = m-1
while any(vi):
    if vi[cnt%n]:
        vi[cnt%n] = False
        answer += str(cnt%n+1)
        cnt += m
    else:
        cnt += 1
print(answer)