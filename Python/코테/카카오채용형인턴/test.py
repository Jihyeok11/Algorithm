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
            myNum = cmd[i][2]
            point += int(myNum)
        elif cmd[i][0]=="U":
            myNum = cmd[i][2]
            point -= int(myNum)
        elif cmd[i][0]=="C":
            if point==len(li)-1:
                res = li.pop(point)
                point -= 1
            else:
                res = li.pop(point)
            bag.append((point,res))
        elif cmd[i][0]=="Z":
            res = bag.pop()
            if point <res[0]:
                point+= 1
            li.insert(res[0],res[1])
    
    res = ["X"]*n
    for i in li:
        res[i] = "O"
    for i in range(len(res)):
        answer += res[i]
        
    return answer