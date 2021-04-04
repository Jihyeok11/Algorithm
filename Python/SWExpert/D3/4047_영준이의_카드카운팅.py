import sys
sys.stdin = open("4047in.txt",'r')

for Count in range(int(input())):
    String = input()
    Card = [[],[],[],[]]
    flag = 0
    for i in range(0,len(String),3):
        shape = String[i]
        if shape=='S':
            if String[i+1:i+3] in Card[0]:
                flag = 1
            else:
                Card[0].append(String[i+1:i+3])
        elif shape=='D':
            if String[i+1:i+3] in Card[1]:
                flag = 1
            else:
                Card[1].append(String[i+1:i+3])
        elif shape=='H':
            if String[i+1:i+3] in Card[2]:
                flag = 1
            else:
                Card[2].append(String[i+1:i+3])
        elif shape=='C':
            if String[i+1:i+3] in Card[3]:
                flag = 1
            else:
                Card[3].append(String[i+1:i+3])
    if flag:
        print("#{} ERROR".format(Count+1))
    else:
        print("#{} ".format(Count+1),end='')
        for i in range(4):
            if i!=3:
                print("{} ".format(13-len(Card[i])),end='')
            else:
                print("{} ".format(13-len(Card[i])))