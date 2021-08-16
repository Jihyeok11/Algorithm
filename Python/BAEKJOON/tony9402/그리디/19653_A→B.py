import sys
from collections import deque
sys.stdin = open("19653in.txt", 'r')

a,b = map(int, sys.stdin.readline().split())
li = deque([(0, a)])
flag = 1
point = 0
ba = set([a])
while 2 ** point < b and li:
    point, a = li.popleft()
    if a == b:
        flag = 0
        print(point + 1)
        break
    if not (a*10 + 1) in ba and ((a*10 + 1) <= b):
        ba.add(a*10 + 1)
        li.append((point+1, a * 10 + 1))
    if not (a*2) in ba and (a * 2 <= b):
        ba.add(a*2)
        li.append((point+1, a * 2))
if flag:
    print(-1)