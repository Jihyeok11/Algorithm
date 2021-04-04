import sys
sys.stdin = open("5986in.txt",'r')

def isPrime(N):
    if (N<2):
        return False
    for i in range(2,N):
        if (N%i)==0:
            return False
    return True

def my_sum(cnt,total,bd):
    global Answer, List,N
    if cnt == 3:
        if total == N:
            Answer += 1
        return
    else:
        for i in range(bd,Length):
            total += List[i]
            my_sum(cnt+1,total,i)
            total -= List[i]

T = int(input())
for Count in range(T):
    N = int(input())
    List = []
    Answer = 0
    for j in range(N):
        if isPrime(j):
            List.append(j)
    Length = len(List)
    my_sum(0,0,0)
    print("#{} {}".format(Count+1,Answer))