import sys
sys.stdin = open("6064in.txt",'r')

for _ in range(int(sys.stdin.readline())):
    m,n,x,y = map(int,sys.stdin.readline().split())
    for i in range(x,m*n+1,m):
        if i%n==y or (i%n==0 and n==y):
            print(i)
            break
    else:
        print(-1)