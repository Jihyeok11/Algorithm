import sys
sys.stdin = open('15650in.txt','r')




N,M = map(int,input().split())
List = []
for i in range(N):
    List.append(i+1)
use_check = [True] * N
Answer= [0 for _ in range(M)]

def bubun(idx):
    if idx != M:
        for i in range(idx,N):
            if use_check[i]:
                use_check[idx] = False
                Numbers[idx] = List[i]
                bubun(idx+1)
                use_check[idx] = True
    else:
        result =1
        for i in range(len(Numbers)):
            for j in range(i+1,len(Numbers)):
                if Numbers[i]>=Numbers[j]:
                    result = 0
        if result:
            print(*Answer)

bubun(0)

