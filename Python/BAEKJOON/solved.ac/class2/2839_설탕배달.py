import sys
sys.stdin = open("2839in.txt",'r')

n = int(sys.stdin.readline())
a = n//5
flag = 1
while a>=0:
    b = (n - (a*5))%3
    if not b:
        print(a+(n-(a*5))//3)
        flag = 0
        break
    else:
        a -= 1
if flag:
    print(-1)