import sys
sys.stdin = open("3282in.txt",'r')

Answer = 0
def basket(cnt,val,bulk):
    global Answer,List
    if val > Answer:
        print(value_basket)
        Answer = val
    if bulk == K: # 현재 부피가 가방 최대 부피면 바로 return
        return

    for i in range(cnt,N):
        if value_basket[bulk+List[i][0]] < val+List[i][1]:
        # if bulk + List[i][0] <= K :
            value_basket[bulk+List[i][0]] = val+List[i][1]
            basket(i+1,val+List[i][1],bulk+List[i][0])

for Count in range(int(input())):
    N,K = map(int,input().split()) # N개, 부피 K 가방
    List = []
    value_basket = [0]*(K+1)
    # value_basket = list(0 for _ in range(K+1))
    for _ in range(N):
        V,C = (map(int,input().split())) # v는 부피, c는 가치
        List.append((V,C))
    basket(0,0,0)
    print(Answer)
    print("#{} {}".format(Count+1,max(value_basket)))

####################################################################################
####################################################################################
####################################################################################

# Answer = 0

# def basket(cnt,val,bulk):
#     global Answer
#     if val > Answer:
#         Answer = val

#     for i in range(cnt,N):
#         if bulk + List[i][0] <= K:
#             basket(i+1,val+List[i][1],bulk+List[i][0])


