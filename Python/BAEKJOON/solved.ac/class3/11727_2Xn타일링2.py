import sys
sys.stdin = open("11727in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = [1,3,5]
if len(li) > n:
    print(li[n-1])
else:
    c = n-len(li)
    while c:
        li.append(li[-1]+2*li[-2])
        c -= 1
    print(li[-1]%10007)