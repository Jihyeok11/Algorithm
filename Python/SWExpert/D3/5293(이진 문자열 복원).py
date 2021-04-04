import sys
sys.stdin = open("5293in.txt",'r')

sheet = ['00','01','10','11']
def Decima(Start):
    global List, Answer,sheet
    if len(Answer)>=2:
        return
    if any(List):
        for j in range(4):
            if List[j] and Start[-1]==sheet[j][0]:
                List[j] -= 1
                Decima(Start+ sheet[j][1])
                List[j] += 1
    else:
        Answer.append(Start)
        return

T = int(input())
for Count in range(T):
    List = list(map(int,input().split()))
    Answer = ['impossible']
    for i in range(4):
        if List[i]:
            Start = str(sheet[i])
            List[i] -= 1
            Decima(Start)
            List[i] += 1
    print("#{} {}".format(Count+1,Answer[-1]))