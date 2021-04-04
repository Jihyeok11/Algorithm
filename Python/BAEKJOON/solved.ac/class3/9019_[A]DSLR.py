import sys
sys.stdin = open("9019in.txt",'r')


from collections import deque
 
for t in range(int(input())):
    visit = [0]*100001
    prev = [-1]*100001
    A, B = map(int,input().split())
    q = deque()
    q.append(A)
    visit[A] = 1
    while q:
        nx= q.popleft()
        if nx == B:
            break
        
        D = (lambda x: 2*x%10000)(nx)
        S = 9999 if (nx ==0) else nx+1
        kiri = len(str(nx)) - 1     #십집수의 길이
        #print(kiri)
        L = (lambda x: x%(10**kiri)*10 + x//(10**kiri))(nx)
        R = (lambda x: x//10 + x%10*(10**kiri))(nx)
        cnt = -1
        for i in [D,S,L,R]:
            cnt += 1    #i를 방문했어도 카운트 해야 하므로 방문체크 위에서 카운트를 한다.
            if visit[i] == 1:
                continue
            q.append(i)
            prev[i] = [nx,cnt]
            visit[i] = 1
            
    path = []
    p = ['D','S','L','R']
    
    while prev[B] != -1:
        path.append(prev[B][1])
        B = prev[B][0]
        
    for i in range(len(path)-1,-1,-1):
        print(p[path[i]], end='')
    print()
            
        