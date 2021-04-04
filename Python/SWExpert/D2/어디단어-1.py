import sys
sys.stdin = open("어디단어in.txt","r")

def p_count(x):
    global count
    for i in range(N):
        nums=[]
        for j in range(N-K+1):
            if j==0:
                nums.append(x[i][0:K])
            elif x[i][j:K+j] == x[i][j-1:K+j-1] == [1]*K:
                nums[-1]=[0]*K
                nums.append([0]*K)
            else :
                nums.append(x[i][j:K+j])
        count += nums.count([1] *K)
    return count

T = int(input())
for ts in range(1,T+1):
    N,K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    verti = []
    for i in range(N):
        a = [puzzle[j][i] for j in range(N)]
        verti.append(a)
    count = 0
    p_count(puzzle)
    p_count(verti)
    print("#{0} {1}".format(ts, count))



# def p_count(x):
#     global count
#     for i in range(N):
#         nums = []
#         for j in range(N - K + 1):
#             if j == 0:
#                 nums.append(x[i][0:K])
#             elif x[i][j:K+j] == x[i][j-1:K+j-1] == [1] * K:
#                 nums[-1] = [0] * K
#                 nums.append([0] * K)
#             else:
#                 nums.append(x[i][j:K+j])
#         count += nums.count([1] * K)
#     return count

# T = int(input())
# for ts in range(1, T+1):
#     N, K = list(map(int, input().split()))
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#     verti = []
#     for i in range(N):
#         a = [puzzle[j][i] for j in range(N)]
#         verti.append(a)
#     count = 0
#     p_count(puzzle)
#     p_count(verti)
#     print('#{0} {1}'.format(ts, count))
