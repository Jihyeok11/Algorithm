import sys
sys.stdin = open("4008in.txt",'r')

def Sachic(idx):
    global List, Answer, Numbers, Max, Min

    if idx==N-1:
        if Max < Answer[-1]:
            Max = Answer[-1]
        if Min > Answer[-1]:
            Min = Answer[-1]

    else:
        for i in range(4):
            if List[i]:
                List[i] -= 1
                A = Answer[-1]
                B = Numbers[idx+1]
                Answer.append(My_Count(A,B,i))
                Sachic(idx+1)
                Answer.pop()                
                List[i] += 1

                
def My_Count(A,B,i):
    if i == 0:
        return A+B
    elif i == 1:
        return A-B
    elif i == 2:
        return A*B
    elif i==3:
        return int(A/B)


T = int(input())
for Count in range(T):
    print("#{0} ".format(Count+1), end='')
    N = int(input()) #5개
    List = list(map(int,input().split())) # + - * //
    Numbers = list(map(int,input().split()))
    Answer = [Numbers[0]]
    Max = -1000000000
    Min = 1000000000
    Sachic(0)
    print(Max)
    print(Min)
    print(Max-Min)