import sys
sys.stdin = open("1541in.txt",'r')

import sys
t = sys.stdin.readline().strip()
if "-" in t:
    te = t.split('-')
else:
    te = [t]
a = te.pop(0)
if "+" in a:
    ans = 0
    b = a.split("+")
    for c in b:
        ans += int(c)
else:
    ans = int(a)
for a in te:
    if "+" in a:
        res = 0
        b = a.split("+")
        for c in b:
            res += int(c)
    else:
        res = int(a)
    ans -= res
print(ans)