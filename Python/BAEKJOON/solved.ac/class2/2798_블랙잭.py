import sys
sys.stdin = open("2798in.txt",'r')

import sys
n,m = map(int,sys.stdin.readline().split())
li = sorted(list(map(int,sys.stdin.readline().split())))

def newJack(li,n):
    myMax = 0
    for i in range(len(li)-2):
        for j in range(i+1,len(li)-1):
            for k in range(j+1, len(li)):
                res = li[i] + li[j] + li[k]
                if res <= n and myMax < res:
                    myMax = res
                if res > n:
                    break
    return myMax
print(newJack(li,m))