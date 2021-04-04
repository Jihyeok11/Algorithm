import sys
sys.stdin = open("3975in.txt",'r')

T = int(input())
answer = []
for _ in range(T):
    name = input().split()
    A,B,C,D = int(name[0]), int(name[1]), int(name[2]), int(name[3])
    a = A/B
    b = C/D
    if a < b:
        answer.append("BOB")
    elif a > b:
        answer.append("ALICE")
    else:
        answer.append("DRAW")
for Count in range(T):
    print("#{} {}".format(Count+1,answer[Count]))