import sys
sys.stdin = open("2292in.txt",'r')

n = int(sys.stdin.readline())
cnt = 0
res = 0
while True:
    if n <= (cnt*6) + 1:
        print(res + 1)
        break
    res += 1
    cnt += res