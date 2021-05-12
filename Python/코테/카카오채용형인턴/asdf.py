from collections import deque
def solution(n, start, end, roads, traps):
    vigo = [True] *(n+1)
    viback = [True]*(n+1)
    vigo[start] = False
    answer = 0
    go = {}
    back = {}
    react = []
    ba = deque([(start,0,react)])
    for i in range(1,n+1):
        go[i] = []
        back[i] = []
    
    for i in roads:
            
        go[i[0]].append((i[1],i[2]))
        back[i[1]].append((i[0],i[2]))
    while ba:
        point,dis,react = ba.popleft()
        if point in traps:
            if point in react: # 이미 발동 되었다면
                react.pop(react.index(point))
            else:
                react.append(point)
        if point==end:
            answer =dis
            break
        if point in react:
            for i in back[point]:
                ba.append((i[0],dis+i[1],react))
        elif not point in react:
            for i in go[point]:
                ba.append((i[0],dis+i[1],react))

        
        
    return answer