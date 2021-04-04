import sys
sys.stdin = open("1288in.txt",'r')

T = int(input())
for Count in range(T):
    N = input()
    List = []
    for i in range(len(N)):
        List.append(N[i])
    Set = set(List)
    N_int = int(N)
    count = 1
    while len(set(List))<10:
        count += 1
        N_str = str(N_int * count)
        for i in range(len(N_str)):
            List.append(N_str[i])
        Answer = int(N_str)
    print("#{0} {1}".format(Count+1,Answer))