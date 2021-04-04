import sys
sys.stdin = open("1205in.txt",'r')

import sys
n,s,p = map(int,sys.stdin.readline().split())
li = list(map(int,sys.stdin.readline().split()))
li.sort(reverse=True)
if s in li:
    idx = li.index(s)
    if idx >= p:
        print(-1)
    else:
        c = li.count(s)
        if idx+c >= p:
            print(-1)
        else:
            print(idx+1)
else:
    for i in range(p):
        try:
            if li[i] < s:
                print(i+1)
                break
        except:
            print(i+1)
            break
    else:
        print(-1)