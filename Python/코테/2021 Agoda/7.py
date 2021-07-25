import sys
sys.stdin = open("7in.txt",'r')

for _ in range(int(input())):
    v = int(input())
    t_y, t_m, t_d, T_y, T_m, T_d = map(int,input().split())
    ba = []
    for _ in range(v):
        ba.append(list(map(int,input().split())))
    print(ba)
    