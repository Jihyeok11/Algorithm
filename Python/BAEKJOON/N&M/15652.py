# import sys
# sys.stdin = open("15652in.txt",'r')

N, M = map(int,input().split())
List = [x+1 for x in range(N)]
Answer = []
def bubun(idx):
    
    if len(Answer) == M:
        print(*Answer)
        return
                    
    else:
        for i in range(idx,N):
            Answer.append(List[i])
            bubun(idx)
            Answer.pop()
            # idx+=1

bubun(0)