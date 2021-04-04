import sys
sys.stdin = open("1946in.txt",'r')

for Count in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = []
    for _ in range(n):
        a,b = map(int,sys.stdin.readline().split())
        li.append((a,b))
    li = sorted(li, key=lambda x: x[0])
    answer = n
    Max = li[0][1]
    for i in range(1,n):
        if Max < li[i][1]:
            answer -= 1
        else:
            Max = li[i][1]
    print(answer)
