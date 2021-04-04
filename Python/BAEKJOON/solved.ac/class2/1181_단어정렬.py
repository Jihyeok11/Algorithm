import sys
sys.stdin = open("1181in.txt",'r')

import sys
n = int(sys.stdin.readline())
ba = set([])
for _ in range(n):
    a = set([sys.stdin.readline().strip()])
    ba = ba|a
li = []
for i in ba:
    li.append(i)
li = sorted(li, key=lambda x:(len(x),x))
for i in li:
    print(i)