
def Up(a,List,weight):
    if a + sum(List) <= weight: ######  a는 다음 트럭 무게
        return True
    return False

def Append(a,List):
    List[0] = a
    return List

def Go(List,bridge_length,weight,i,count,truck_weights):
    for count in range(bridge_length-1,0,-1):
        List[count] = List[count-1]
    if (sum(List[1:]) + truck_weights[i+1]) <= weight:
        Append(truck_weights[i+1],List)
    elif (sum(List[1:]) + truck_weights[i+1]) > weight:
        List[0] = 0
    count += 1
    return List,count,i
    
def solution(bridge_length, weight, truck_weights):
    List = [0]*bridge_length
    truck_weights.append(0)
    i=0
    count = 0
    Append(a,List)
    while i <=(len(truck_weights)-1):
        a = truck_weights[i]  #a는 선택된 트럭
        Go(List,bridge_length,weight,i,count,truck_weights)



    
solution(5,10,[7,4,5,6])








