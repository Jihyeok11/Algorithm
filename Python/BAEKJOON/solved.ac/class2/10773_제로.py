import sys
sys.stdin = open("10773in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a:
        li.append(a)
    else:
        if li:
            li.pop()
        else:
            pass
print(sum(li))