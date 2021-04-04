import sys
sys.stdin = open("1992in.txt",'r')

import sys

def sq(n,a,b):
    global ans
    s = li[a][b]
    for y in range(n):
        for x in range(n):
            if li[a+y][b+x] != s:
                break
        if li[a+y][b+x] != s:
            break
    else:
        ans += str(s)
        return
    ans += "("
    sq(n//2,a,b)
    sq(n//2,a,b+n//2)
    sq(n//2,a+n//2,b)
    sq(n//2,a+n//2,b+n//2)
    ans += ")"
n = int(sys.stdin.readline())
ans = ""
li = list(list(int(x) for x in sys.stdin.readline().strip()) for _ in range(n))
sq(n,0,0)
print(ans)