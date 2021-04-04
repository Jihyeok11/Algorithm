def solution(Str):

    List = []
    for i in range(len(Str)):
        List.append(Str[i])

    Max_List = []
    for i in range(len(Str)):
        idx = List.index(max(List))
        Max_List.append(List.pop(idx))
    A = "".join(Max_List)
    numbers = int(A)
    # print(numbers)
   
    answer = 0


    
    Prime = [False]*2 + [True]*(numbers-1)
    PL = []
    for i in range(2,numbers+1):
        if Prime[i]==True:
            PL.append(str(i))
            for j in range(i+i,numbers+1,i):
                Prime[j] = False

    print(PL)

    
       ##에라토스테네스
    # Prime_List = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97', '101', '103', '107', '109']

    Prime_2List = [[] for _ in range(len(PL)) ]
    # print(Prime_2List)
    for i in range(len(PL)):
        for j in range(len(PL[i])):
            Prime_2List[i].append(PL[i][j])

    # print(Prime_2List)## 2단 배열로 소수들을 자리수별로 나눔
    for l in range(len(Prime_2List)):
        for j in range(len(Str)):   #1과 7
            value = Str[j]
            if value in Prime_2List[l]:
                idx = Prime_2List[l].index(value)
                Prime_2List[l].pop(idx)
    for i in Prime_2List:
        if not i:
            answer += 1

    return print(answer)

solution("17")