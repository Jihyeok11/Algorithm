import sys
sys.stdin = open("1966in.txt", 'r')

def pri(m):
    cnt = point = 0
    lv = 9
    while lv:
        for i in range(n):
            if li[(point + i) % n][1] == lv:
                tp = (point + i) % n
                cnt += 1
                if li[tp][0] == m:
                    return cnt
        lv -= 1
        try:
            point = tp
        except:
            pass

for _ in range(int(sys.stdin.readline())):
    n, m = map(int,sys.stdin.readline().split())
    t = list(map(int,input().split()))
    li = []
    for i in range(n):
        li.append((i,t[i]))
    print(pri(m))