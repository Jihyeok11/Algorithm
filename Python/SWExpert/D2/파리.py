
import sys
sys.stdin = open("파리in.txt", 'r')
T = int(input())
for count in range(T):
    N,M = map(int,input().split())
    List = [0]*N
    LIST=[]
    for i in range(N):
        List[i] = list(map(int,input().split()))
    for idx_x in range(0,N-M+1): #x는 0부터 N-M+1까지 (0,4)
        for idx_y in range(0,N-M+1):
            A=0
            for c in range(M):
                for d in range(M):
                    A +=List[idx_x+c][idx_y+d]
            
            LIST.append(A)
    print("#{0} {1}".format(count+1,max(LIST)))



# T = int(input())
# for count in range(T):
#     Str = input()
#     A = 0
#     if Str == Str[::-1]:
#         A = 1
#     print("#{0} {1}".format(count+1, A))