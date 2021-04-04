def solution(boxes):
    items = []# [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8]
    for i in boxes:
        A,B = i
        items.append(A)
        items.append(B)
    items.sort()    # print(items.count(5)) # 2개
    odd = 0 # 총 홀수개
    even = 0 # 총 짝수 개
    my_set = set(items)
    for i in my_set:
        result = items.count(i)
        if result%2: # 홀수개이면
            odd += 1
        else: # 짝수개이면
            even += result

    answer = (len(items)-even)//2
    print(answer)
    return answer







boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
result = 2
solution(boxes)