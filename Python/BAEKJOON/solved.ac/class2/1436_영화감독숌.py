import sys
sys.stdin = open("1436in.txt",'r')

n = int(sys.stdin.readline().strip())
cnt = 1
a = 666
while True:
    if cnt == n:
        print(a)
        break
    a += 1
    if "666" in str(a):
        cnt += 1