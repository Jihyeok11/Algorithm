import sys
sys.stdin = open("1949in.txt",'r')

import sys
sys.getrecursionlimit(3000)
def my_part(res,cnt,n):
    if cnt == n:
        part.append(res)
        return
    my_part(res+[False],cnt+1,n)
    my_part(res+[True],cnt+1,n)

def find_usoo(List):
    for i in range(n):
        if List[i]:
            for j in route[i]:
                if List[j]:
                    return False
        else:
            for j in range(n):
                if (i in route[j]) and List[j]:
                    break
            else:
                return False
    return True
n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
route = {}
for i in range(n):
    route[i] = []
for _ in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    route[a].append(b)
    route[b].append(a)
part = []
my_part([],0,n)
cnt = 1
ans = 0
for myList in part:
    if find_usoo(myList):
        res = 0
        for i in range(len(myList)):
            if myList[i]:
                res += li[i]
        if res > ans:
            ans = res
print(ans)