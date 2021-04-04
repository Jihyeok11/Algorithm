def solution(answer):
    
    
    P1 = [1,2,3,4,5]
    len_P1 = len(P1) #len_P1 = 6
    P2 = [2, 1, 2, 3, 2, 4, 2, 5]
    len_P2 = len(P2) #len_P2 = 9
    P3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_P3 = len(P3) #len_P1 = 11
    len_answer = len(answer)  #answers를 [1,2,3,4,5]로 입력하면 길이는 5=
     # 6으로 나눈다
    count_P1 = 0
    count_P2 = 0
    count_P3 = 0

    for i in range(len_answer):

        if i> 4: #인덱스가 5가 되면
            P1.append(P1[((i)%len_P1)])
        if answer[i]==P1[i]:
            count_P1 += 1

    for i in range(len_answer):

        if i> 7: #인덱스가 8가 되면
            P2.append(P2[((i)%len_P2)])
        if answer[i]==P2[i]:
            count_P2 += 1

    for i in range(len_answer):

        if i> 9: #인덱스가 10가 되면
            P3.append(P3[((i)%len_P3)])
        if answer[i]==P3[i]:
            count_P3 += 1
    
    print(count_P1,P2,count_P3)
    if count_P1>count_P2 and count_P1>count_P3:
        return [1]
    elif count_P2>count_P3 and count_P2>count_P1:
        return [2]
    elif count_P3>count_P1 and count_P3>count_P2:
        return [3]
    elif count_P3==count_P1 and count_P3>count_P2:
        return [1,3]
    elif count_P3==count_P2 and count_P3>count_P1:
        return [2,3]
    elif count_P2==count_P1 and count_P2>count_P3:
        return [1,2]
    elif count_P2==count_P1==count_P3:
        return [1,2,3]