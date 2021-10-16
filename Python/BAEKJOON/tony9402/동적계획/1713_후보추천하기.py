import sys
from collections import defaultdict
sys.stdin = open("1713in.txt",'r')

n = int(sys.stdin.readline())
st = int(sys.stdin.readline())
rec_st = defaultdict(int)
li = list(map(int, sys.stdin.readline().strip().split()))
lastpick = []
ba = []
for i in li:
    lastpick.append(i)
    if len(ba) < n:
        if not i in ba:
            ba.append(i)
        rec_st[i] += 1
    else:
        rec_st[i] += 1