import sys
sys.stdin = open("3809in.txt",'r')

for Count in range(int(input())):
    Number = int(input())
    Shit = []
    while len(Shit)<Number:
        Shit += list(map(int,input().split()))
    Answer = 0
    while True:
        if Answer in Shit:
            Answer += 1
        else:
            break
    if Answer>=10:
        AShit = []
        for i in range(Number-1):
            AShit.append(Shit[i]*10+Shit[i+1])
        while True:
            if Answer in AShit:
                Answer += 1
            else:
                break
    if Answer>= 100:
        BShit = []
        for i in range(Number-2):
            BShit.append(Shit[i]*100 + Shit[i+1]*10 + Shit[i+2])
        while True:
            if Answer in BShit:
                Answer += 1
            else:
                break

    print("#{} {}".format(Count+1,Answer))