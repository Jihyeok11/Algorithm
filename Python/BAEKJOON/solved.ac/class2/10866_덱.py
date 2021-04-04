import sys
sys.stdin = open("10866in.txt",'r')

import sys
from collections import deque
n = int(sys.stdin.readline())
li = deque([])
for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if a[-1].isdigit():
        a,b = a.split()
    if a =="push_front":
        li.appendleft(b)
    elif a=="push_back":
        li.append(b)
    elif a=="pop_front":
        if li:
            print(li.popleft())
        else:
            print(-1)
    elif a=="pop_back":
        if li:
            print(li.pop())
        else:
            print(-1)
    elif a=="size":
        print(len(li))
    elif a=="empty":
        if li:
            print(0)
        else:
            print(1)
    elif a=="front":
        if li:
            print(li[0])
        else:
            print(-1)
    elif a=="back":
        if li:
            print(li[-1])
        else:
            print(-1)