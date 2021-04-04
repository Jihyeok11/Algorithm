def solution(Str):
    numbers = int(Str)
    Prime_List = []
    for i in range(2,numbers):
        count = 0
        for j in range(1,i):
            if i%j==0:
                count +=1
        if count ==1:
            Prime_List.append(j)
    answer = 0
    return answer

solution("17")