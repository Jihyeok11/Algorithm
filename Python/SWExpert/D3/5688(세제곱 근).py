import sys
sys.stdin = open("5688in.txt",'r')

def My_Tri(N):
    for i in range(10**18):
        if i**3 > N:
            return -1
        elif i**3 == N:
            return i

T = int(input())
for Count in range(T):
    N = int(input())
    Answer = My_Tri(N)
    print("#{} {}".format(Count+1,Answer))
