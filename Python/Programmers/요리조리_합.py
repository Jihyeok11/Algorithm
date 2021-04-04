List = [1,1,1,0,0,0,1]
basket = []
for i in range(len(List)):
    if List[i]:
        basket.append(i)

basket = [0,1,2,6]
Basket = []
whole = []
visited = [True] * 4
def part(Basket,cnt):
    global basket
    if cnt == len(basket):
        whole.append(Basket)
    for i in range(len(basket)):
        if visited[i]:
            visited[i] = False
            part(Basket+[basket[i]],cnt+1)
            visited[i] = True

part([],0)
Min = 100000
for i in range(len(whole)):
    my_List = whole[i]
    result = 0
    start = my_List[0]
    for i in range(1,len(my_List)):
        result += min(abs(my_List[i]-start), start+(len(List)-my_List[i]))
        start = my_List[i]
    if result+my_List[0] < Min:
        Min = result
        print(my_List,Min)