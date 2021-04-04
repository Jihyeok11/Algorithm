import sys
sys.stdin = open("in.txt",'r')

def partition(List):
    for i in range(1,N-M+1+1): # i는 1부터 6까지 가능
        if sum(List) > N:
            return
        elif len(List) == M-1 and sum(List)+1 <= N: # 마지막에는
            List.extend([N - sum(List)])
            myBasket.extend([List])
            return
        else:
            partition(List + [i])

N,M = map(int,input().split())
if N == 8 or N==4:
    beeds = list(map(int,input().split()))
myBasket = []
partition([])
answer = 10000000
for myList in myBasket: # myList = [3, 1, 3, 1],
    myBeeds = beeds[:]
    basket = []
    for howmany in myList:
        result = 0
        for _ in range(howmany):
            result += myBeeds.pop(0)
        basket.append(result)
    Max = max(basket)
    if answer > Max:
        answer = Max
print(answer)
# # -----
# # 8은 공 개수 N
# # 3은 칸 개수 M