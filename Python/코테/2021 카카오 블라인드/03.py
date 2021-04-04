def solution(info, query):
    answer = []
    for j in range(len(query)):
        want = 0
        lan,second,nd,fourth,ior,sixth,od,ore = query[j].split()

        for i in range(len(info)):
            language,end,nior,food,score = info[i].split()
            if lan == language or lan=="-":
                if nd == "-" or  nd == end:
                    if ior == "-" or nior == ior:
                        if od == "-" or  od == food:
                            if int(score) >= int(ore):
                                want += 1
        answer.append(want)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info,query)

# answer = [1,1,1,1,2,4]