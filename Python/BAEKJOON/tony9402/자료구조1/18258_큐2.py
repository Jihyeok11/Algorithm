import sys
from collections import deque
sys.stdin = open("18258in.txt",'r')

n = int(sys.stdin.readline())
ba = deque([])
for _ in range(n):
    order = sys.stdin.readline().strip()
    if order[-1].isdigit():
        order, num = order.split()
    if order == "push":
        ba.append(num)
    elif order == "pop":
        if ba:
            print(ba.popleft())
        else:
            print(-1)
    elif order == "size":
        print(len(ba))
    elif order == "empty":
        if ba:
            print(0)
        else:
            print(1)
    elif order == "front":
        if ba:
            print(ba[0])
        else:
            print(-1)
    elif order == "back":
        if ba:
            print(ba[-1])
        else:
            print(-1)