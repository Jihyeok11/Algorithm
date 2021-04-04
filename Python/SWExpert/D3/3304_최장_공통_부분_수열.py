import sys
sys.stdin = open("3304in.txt",'r')

Max = answer = 0

def longestPart(A,B,Max):
    global answer
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                Max += 1
                if Max > answer:
                    answer = Max
                longestPart(A[i+1:],B[j+1:],Max)
                Max -= 1

for Count in range(int(input())):
    A,B = input().split()
    Max = 0
    answer = 0
    longestPart(A,B,0)



    print("#{} {}".format(Count+1,answer))