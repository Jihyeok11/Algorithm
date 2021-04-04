import sys
sys.stdin = open("1204in.txt",'r')


T = int(input())
for Count in range(T):
    N = int(input())
    List = list(map(int,input().split()))
    Max = max(List)
    Value = 0
    Answer_List = [0]*(Max+1)
    for i in range(Max+1):
        Answer_List[i] = List.count(i)
    for j in range(Max,-1,-1):
        if Answer_List[j]==max(Answer_List):
            Answer = j
            break
    print("#{0} {1}".format(Count+1, Answer))

    #     if Value > Answer:
    #         Answer = Value
    # 