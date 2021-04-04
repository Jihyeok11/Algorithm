def solution(n, lost, reserve):
    List = [1]*n
    for i in range(len(reserve)):
        List[reserve[i]-1] += 1
    for i in range(len(lost)):
        List[lost[i]-1] -= 1

    for i in range(len(lost)):
        if i==0:
            if List[i]==0:
                if List[1]==2:
                    List[1]-=1
                    List[0]=1
        elif i == len(lost)-1:
            if List[i]==0:
                if List[len(List)-2]==2:
                    List[len(List)-2] -= 1
                    List[len(List)-1]=1
        
        else:
            if List[lost[i]-1]==0:
                if List[lost[i]-2]==2: #일단 앞사람한테 빌리고
                    List[lost[i]-2] -= 1
                    List[lost[i-1]] = 1
                    pass
            
                elif List[lost[i]]==2: #앞사람 없으면 뒷사람한테 빌린다.
                    List[lost[i]+1] -= 1
                    List[lost[i-1]] = 1
                    pass
    answer = List
        
    return answer 
