    import sys
    sys.stdin = open("어디단어in.txt","r")
T = int(input())

for count in range(T): #T번 count
    N, K = map(int, input().split())
    Answer=0
    List = [list(map(int,input().split())) for x in range(N)]
    
    
    for i in range(N):#N개 중에서
        Counts = 0
        Answer_Listx = []
        for j in range(N):
            
            if List[i][j]==0:
                if Counts == 0:
                    Answer_Listx.append(0)
                else :
                    Answer_Listx.append(Counts)
                    Answer_Listx.append(0)
                    Counts=0
            elif j==N-1:
                if List[i][j]==1:
                    Counts += 1
                    Answer_Listx.append(Counts)
            elif List[i][j]==1:
                Counts += 1
        for i in Answer_Listx:
            if i==K:
                Answer += 1
        
    
    for i in range(N):
        Answer_Listy = []
        Counts=0
        for j in range(N): #N개의 칸중에서 (가로)
            if List[j][i]==0:
                if Counts ==0:
                    Answer_Listy.append(0)
                else :
                    Answer_Listy.append(Counts)
                    Answer_Listy.append(0)
                    Counts=0
            elif j==N-1:
                if List[j][i]==1:
                    Counts += 1
                    Answer_Listy.append(Counts)
            elif List[j][i]==1:
                Counts += 1
        for i in Answer_Listy:
            if i==K:
                Answer += 1
   
    print("#{0} {1}".format(count+1, Answer))