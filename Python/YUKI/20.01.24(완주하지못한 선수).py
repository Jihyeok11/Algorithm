def solution(participant, completion):
    
    Dict_part = {} 
    for i in participant:
        if not i in Dict_part:
            Dict_part[i] = 1
        elif  i in Dict_part:
            Dict_part[i] += 1
    
    Dict_comp = {}
    for i in completion:
        if not i in Dict_comp:
            Dict_comp[i] = 1
        elif  i in Dict_comp:
            Dict_comp[i] += 1
    
    for key,value in Dict_part.items():
        if key not in Dict_comp or value - Dict_comp[key]==1:
            return print(key)

solution(['leo','kiki','eden'], ['eden','kiki'])