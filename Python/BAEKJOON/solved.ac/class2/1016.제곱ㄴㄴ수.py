import sys
sys.stdin = open("1016in.txt",'r')

import sys
def era(a,b):
    global answer
    for i in range(2,int(b**0.5)+1):
        for j in range(i**2,b+1,i**2):
            if j<a:
                continue
            if li[j-a]:
                li[j-a] = False
                answer += 1

a,b = map(int,sys.stdin.readline().split())
li = [True]*(b-a+1)
answer = 0
era(a,b)
print(answer)