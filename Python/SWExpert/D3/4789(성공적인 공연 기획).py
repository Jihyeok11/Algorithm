import sys
sys.stdin = open("4789in.txt",'r')

T = int(input())
for Count in range(T):
    Input = [int(x) for x in input()]
    sum = 0
    add = 0
    for i in range(len(Input)):
        if i <= sum:
            sum += Input[i]
        else:
            while sum+add < i:
                add +=1
            sum += Input[i]
    print("#{} {}".format(Count+1,add))