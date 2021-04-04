import sys
sys.stdin = open("3307in.txt",'r')

def lis(a):
    d = [0] * (N)
    for i in range(1,N):    
        for j in range(i):
            if a[i] > a[j]:
                d[i] = max(d[i],d[j]+1)
    return max(d)

for t in range(int(input())):
    N = int(input())
    a_list = list(map(int, input().split()))
    print(f"#{t+1} {lis(a_list)+1}")