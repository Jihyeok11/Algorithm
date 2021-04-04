import sys
sys.stdin = open('2579in.txt','r')

N = int(input())
List = []

for i in range(N):
    List.append(int(input()))
Answer = [0 for _ in range(N)]

def stair():
    for i in range(N):
        
        if i==0:
            Answer[i] = List[i]
        elif i==1:
            Answer[i] = Answer[i-1] + List[i]
        elif i == 2:
            Answer[i] = max(List[i-1]+List[i] , List[i-2]+ List[i])
        else:
            Answer[i] = max(Answer[i-2]+List[i] , Answer[i-3] + List[i-1] + List[i])
    print(Answer[-1])
stair()