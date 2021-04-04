import sys
sys.stdin = open("3750in.txt",'r')

T = int(input())
Answer = []
for Count in range(T):
    Number = int(input())
    while Number>=10:
        Reference = str(Number)
        Number = 0
        for i in range(len(Reference)):
            Number += int(Reference[i])
    Answer.append(Number)
for i in range(T):
    print("#{} {}".format(i+1,Answer[i]))