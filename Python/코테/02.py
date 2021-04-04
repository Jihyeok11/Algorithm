def solution(orders, course):
    menus = []
    answer = []
    for i in orders:
        for j in i:
            if not j in menus:
                menus.append(j)
    menus.sort()
    # menus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    Result = [[]] # 256개
    for n in menus:
        for p in range(len(Result)):
            if not Result[p]+[n] in Result:
                Result.append(Result[p]+[n])
    # Wls = []
    # for q in Result:
    #     for r in course:
    #         if len(q)==r:
    #             Wls.append((r,q))
    # Wls.sort() # 156개 , (2, ['B', 'C']),

    for m in course:

        Max = 1
        product = []
        for i in Result: # i는 (2, ['B', 'C'])
            if len(i) == m: # 2일 때, 3일때, 4일 때,
                Yes = 0
                for k in range(len(orders)):
                    # k는 "ABDFG","AC","CDE","ACDE", "BCFG", "ACDEH"
                    List = i # "['B','C']"
                    Count = 0

                    for z in List:
                        if z in orders[k]:
                            Count += 1

                    if Count == len(List):
                        Yes += 1
                    if Yes > Max:
                        Max = Yes
                        product = [ ''.join(i)]
                    elif Yes == Max and Yes>1:
                        if not ''.join(i) in product:
                            product.append(''.join(i))

        for i in product:
            answer.append(i)         

    answer.sort()
    # print(answer)
    return answer


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# orders = ["XYZ", "XWY", "WXA"]

# course = [2,3,4]
course = [2,3,5] 
# course = [2, 3, 4]
solution(orders,course)