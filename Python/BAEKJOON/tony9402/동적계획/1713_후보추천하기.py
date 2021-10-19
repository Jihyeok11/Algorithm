import sys
from collections import defaultdict
sys.stdin = open("1713in.txt",'r')

n = int(sys.stdin.readline())
st = int(sys.stdin.readline())
rec_st = defaultdict(int)
check_li = defaultdict(int)
li = list(map(int, sys.stdin.readline().strip().split()))
ba = []
for i in range(st):
    rec_st[li[i]] += 1
    if not li[i] in ba:
        check_li[li[i]] = i
        if len(ba) < n:
            ba.append(li[i])
        else:
            tp = []
            for j in ba:
                tp.append([rec_st[j], check_li[j], j])
            tp = sorted(tp, key=lambda x:(-x[0], -x[1]))
            rm_idx = tp[-1][2]
            rec_st[rm_idx] = 0
            ba.pop(ba.index(rm_idx))
            ba.append(li[i])
ba.sort()
print(*ba)