import sys
sys.stdin = open("4299in.txt",'r')

for Count in range(int(input())):
    D,H,M = map(int,input().split())
    D -= 11
    H -= 11
    M -= 11
    while M < 0:
        H -= 1
        M += 60
    while H < 0:
        D -= 1
        H += 24
    if D < 0:w
        print("#{} -1".format(Count+1))
        break
    Answer = M + (H + D*24)*60
    print("#{} {}".format(Count+1,Answer))