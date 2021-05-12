def solution(n, k, cmd):
    vi = [True] *(n)
    answer = ''
    myNum = 0
    point = k
    li = []
    bag = []
    for i in range(n):
        li.append(i)
    for i in range(len(cmd)):
        if cmd[i][0]=="D":
            myNum = int(cmd[i][2])
            cnt = 0
            while cnt<myNum:
                if vi[point]:
                    point+=1
                    cnt+=1
                
        elif cmd[i][0]=="U":
            myNum = int(cmd[i][2])
            cnt = 0
            while cnt<myNum:
                if vi[point]:
                    point -= 1
                    cnt += 1
        elif cmd[i][0]=="C":
            vi[point] = False
            point -= 1
            bag.append(point)
        elif cmd[i][0]=="Z":
            res = bag.pop()
            vi[res]=True
    
    res = ["X"]*n
    for i in li:
        res[i] = "O"
    for i in range(len(res)):
        answer += res[i]
        
    return answer


# solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"])
solution(8, 7, ["C","U 1","C","U 1","C"])
# "OOOOXOOO"