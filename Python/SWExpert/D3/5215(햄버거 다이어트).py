import sys
sys.stdin = open("5215in.txt",'r')
################################## 20개 중 16개 맞았
# T = int(input())
# for Count in range(T):
#     N,L = map(int,input().split())

#     Answer = [(0,0)]
#     Max = 0
#     for _ in range(N):
#         score, cal = map(int,input().split())
#         for i in range(len(Answer)):
#             if Answer[i][1]+cal <= L:
#                 Answer.append((Answer[i][0]+score,Answer[i][1]+cal))
#                 if Max < Answer[i][0]+score:
#                     Max = Answer[i][0]+score
#     print("#{} {}".format(Count+1,Max))

#위의 식은 런타임 에러로 안되네
# 이젠 그냥 부분집합으로 풀어보자



# T = int(input())
# for Count in range(T):
#     N,L = map(int,input().split())

#     Answer = [(0,0)]
#     Max = 0
#     result = [0]
#     for _ in range(N):
#         score, cal = map(int,input().split())
#         for i in range(len(Answer)):
#             if Answer[i][1]+cal <= L:
#                 Answer.append((Answer[i][0]+score,Answer[i][1]+cal))
#                 result.append(Answer[i][0]+score)
#     Max = max(result)
#     print("#{} {}".format(Count+1,Max))

### score, cal을 따로따로 리스트에 담자
T = int(input())
for Count in range(T):
    N,L = map(int,input().split())
    score_list = [0]
    cal_list = [0]
    for _ in range(N):
        score, cal = map(int,input().split())
        F_score_list = score_list[:]
        F_cal_list = cal_list[:]
        if cal > L:
            continue
        for i in range(len(score_list)):
            if cal_list[i] + cal <= L:
                if cal_list[i]+cal in cal_list:
                    idx = cal_list.index(cal_list[i]+cal)
                    if score_list[idx] < score_list[i]+score: # ? vs 300
                        F_score_list[idx] = F_score_list[i]+score
                else:
                    F_score_list.append(score_list[i]+score)
                    F_cal_list.append(cal_list[i]+cal)
        score_list = F_score_list[:]
        cal_list = F_cal_list[:]
    
    print("#{} {}".format(Count+1,max(score_list)))

# def beerg(cnt):
#     global Max
#     if cnt >= N:
#         sum = 0
#         score = 0
#         for i in range(N):
#             if not Visited[i]:# False일 때만 합치자
#                 sum += List[i][1]
#                 score += List[i][0]
#                 if sum > L:
#                     break
#             if score > Max:
#                 Max = score
#     else:
#         Visited[cnt] = True
#         beerg(cnt+1)
#         Visited[cnt] = False
#         beerg(cnt+1)


#     return Max


# T = int(input())
# for Count in range(T):
#     N,L = map(int,input().split())
#     List = [list(map(int,input().split())) for _ in range(N)]
#     Visited = [True] * N
#     Max = 0
#     Max = beerg(0)
#     print(Max)
    

















#################################20개중 9개

##### 이 전에 풀었는데 왜 오늘은 안되냐

# def Berrrg(idx,_sum,Cal):
#     global Max
    
#     if idx != N:
#         if not use_check[idx]:
#             use_check[idx] = True
#             Berrrg(idx+1,_sum,Cal)
#             use_check[idx] = False
#             Berrrg(idx+1,_sum,Cal)
#     if idx == N:
#         # use_check[i] 모든 부분집합
#         Cal = 0
#         total = 0
#         for i in range(N):
#             if use_check[i]: #True일 때
#                 Cal += List[i][1]
#                 total += List[i][0]
#                 if Cal > Limit:
#                     break
#             if total > Max:
#                 Max = total

                

# T = int(input())
# for Count in range(T):
#     print("#{0} ".format(Count+1),end='')
#     N , Limit = map(int,input().split())
#     use_check = [False] * N
#     List = []
#     for i in range(N):
#         A,B = map(int,input().split())
#         List.append((A,B))
#     Max = 0
#     Berrrg(0,0,0)
#     print(Max)