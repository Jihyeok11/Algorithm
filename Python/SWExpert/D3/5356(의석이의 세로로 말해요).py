import sys
sys.stdin = open("5356in.txt",'r')

T = int(input())
for Count in range(T):
    Str = [0 for _ in range(5)]
    Max = 0
    for i in range(5):
        Str[i] = input()
        if Max < len(Str[i]):
            Max = len(Str[i])
    Answer = ''
    for i in range(5):
        while len(Str[i])<Max:
            Str[i] +='?'
    for i in range(Max):
        for j in range(5):
            Answer += Str[j][i]
    Answer = Answer.replace("?","")
    print("#{} {}".format(Count+1,Answer))