import sys
sys.stdin = open("1946in.txt",'r')

T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1))
    N = int(input())
    STR = ''
    for i in range(N):
        A,B = input().split()
        B = int(B)
        STR += A*B
    print(type(STR))
    for j in range((len(STR)//10)+1):
        print((STR[10*j:10*(j+1)]))
