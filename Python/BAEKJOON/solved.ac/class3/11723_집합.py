import sys
sys.stdin = open("11723in.txt",'r')

import sys
vi = [True] * 21
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().strip()
    if a[-1].isdigit():
        a,b = a.split()
        b = int(b)
    if a=="add":
        vi[b] = False
    elif a=="remove":
        vi[b] = True
    elif a=="check":
        if vi[b]:
            print(0)
        else:
            print(1)
    elif a == "toggle":
        if vi[b]:
            vi[b] = False
        else:
            vi[b] = True
    elif a =="all":
        vi = [False] * 21
    elif a == "empty":
        vi = [True] * 21