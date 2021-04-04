import sys
sys.stdin = open("5948in.txt",'r')

def part(cnt,Total):
    global Answer_List,List
    if cnt == 3:
        if not Total in Answer_List:
            Answer_List.append(Total)
        return
    else:
        for i in range(len(List)):
            if Visited[i]:
                Visited[i] = False
                Total += List[i]
                part(cnt+1,Total)
                Total -= List[i]
                Visited[i] = True

    

T = int(input())
for Count in range(T):
    List = list(map(int,input().split()))
    Visited = [True]*len(List)
    Answer_List = []
    part(0,0)
    Answer_List.sort()
    print("#{} {}".format(Count+1,Answer_List[-5]))
