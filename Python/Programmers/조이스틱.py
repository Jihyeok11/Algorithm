def part(visited,basket,Basket,cnt,whole):
    if cnt == len(basket):
        whole.append(Basket)

    for i in range(len(basket)):
        if visited[i]:
            visited[i] = False
            part(visited,basket,Basket+[basket[i]],cnt+1,whole)
            visited[i] = True

def solution(name):
    basket = []
    for i in range(len(name)):
        if name[i]!="A":
            basket.append(i)
    if basket[0] != 0:
        basket = [0]+basket
    visited = [True] * len(basket)
    whole = []
    part(visited,basket,[],0,whole)
    
    Min = 100000
    for sel in range(len(whole)):
        myList = whole[sel]
        result = 0
        start = myList[0]
        for i in range(1,len(myList)):
            result += min(abs(len(name)+start-myList[i]),abs(myList[i]-start),abs(len(name)-start+myList[i]))
            start = myList[i]
            if result > Min:
                break


        if result+myList[0] < Min:
            Min = result
            minList = myList
    
    answer = Min
    for i in range(len(minList)):
        num = ord(name[minList[i]])-64
        answer += min(num-1,27-num)

    return answer




name = "AAAAAAAB" # 8, 2
name = "JEROEN"
name = "AAAAAABAAA" # 7, 5
name = "JAZ"
print(solution("KJEAZAAN"))
print(solution(name))
print(solution("BBBAAAB"))#9
print(solution("AZAAAZ"))#9