import sys
sys.stdin = open("9375in.txt",'r')

import sys
for _ in range(int(sys.stdin.readline())):
    cl = {}
    for _ in range(int(sys.stdin.readline())):
        a,b = sys.stdin.readline().split()
        if not b in cl:
            cl[b] = [a]
        else:
            cl[b].append(a)
    ans = 1
    for i in cl:
        ans *= len(cl[i])+1
    print(ans-1)