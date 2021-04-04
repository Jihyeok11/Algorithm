import sys
sys.stdin = open("5515in.txt",'r')

T = int(input())
for Count in range(T):
    List =[0,31,29,31,30,31,30,31,31,30,31,30,31]
    m,d = map(int,input().split())
    day = 3
    for i in range(m):
        day += List[i]
    day += d
    day %= 7
    print("#{} {}".format(Count+1,day))
