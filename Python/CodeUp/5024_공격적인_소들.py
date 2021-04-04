import sys
sys.stdin = open("in.txt",'r')

def part(cnt,myList):
    if cnt == cows:
        basket.append(myList)
    else:
        for i in range(cnt,N):
            if visited[i]:
                visited[i] = False
                part(cnt+1,myList+[List[i]])
                visited[i] = True

N,cows = map(int,input().split())
List = []
for _ in range(N):
    List.append(int(input()))
basket = []
visited = [ True for _ in range(N) ]
part(0,[])
