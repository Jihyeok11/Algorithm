import sys
sys.stdin = open("5525in.txt",'r')

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
st = sys.stdin.readline().strip()
ans = 0
fit = "IO" * n + "I"
l = 0
while l < m-2*n:
    if st[l]=="I" and st[l:l+1+2*n]==fit:
        ans += 1
        r = l+2*n+1
        while True:
            if st[r:r+2]=="OI":
                r += 2
                ans += 1
            else:
                l = r
                break
    else:
        l += 1
print(ans)