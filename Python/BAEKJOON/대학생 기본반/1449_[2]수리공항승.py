import sys
sys.stdin = open("1449in.txt",'r')
import sys
n,l = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort()
vi = [False]*(li[-1]+1)
answer = 0
for i in li:
    vi[i] = True
for i in li:
    if vi[i]:
        answer += 1
        try:
            for j in range(l):
                vi[i+j] = False
        except:
            pass
print(answer)