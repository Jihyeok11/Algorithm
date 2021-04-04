import sys
sys.stdin = open("1966in.txt",'r')

import sys
for count in range(int(sys.stdin.readline())):
    # print(count+1, end=" ")
    n,m = map(int,sys.stdin.readline().split())
    ba = list(map(int,sys.stdin.readline().split()))
    li = []
    wants = ba[m]
    for i in range(len(ba)):
        li.append((i,ba[i]))
    cnt = 9
    flag = 1
    ans = 0
    while flag and cnt:
        last = 0
        for i in range(len(li)):
            if li[i][1] == cnt:
                ans += 1
                last = i
                if li[i][0] == m:
                    print(ans)
                    flag = 0
                    break
        li = li[last:] + li[:last]
        cnt -= 1