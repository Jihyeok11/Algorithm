def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        List = list(map(int,commands[i])) #List = [2,5,3]
        A = List[0]
        B = List[1]
        C = List[2]
        List = array[A-1:B]
        List.sort()
        answer.append(List[C-1])
        
    
    return print(answer)