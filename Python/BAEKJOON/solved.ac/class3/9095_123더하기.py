import sys
sys.stdin = open("9095in.txt",'r')

c = [1,2,3]
def ma(res):
    global ans
    if res > n:
        return
    elif res == n:
        ans += 1
        return
    for i in range(3):
        ma(res+c[i])
    
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ans = 0
    ma(0)
    print(ans)