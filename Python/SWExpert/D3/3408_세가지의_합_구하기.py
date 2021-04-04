import sys
sys.stdin = open("3408in.txt",'r')

T = int(input())
for Count in range(T):
    Number = int(input())
    C1 = 0
    Answer = Number*(Number+1)//2
    print("#{} {} {} {}".format(Count+1,Answer, 2*Answer-Number, 2*Answer))
    