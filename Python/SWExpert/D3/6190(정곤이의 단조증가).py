import sys
sys.stdin = open("6190in.txt",'r')

def danzo(data):
    result = data
    while data:
        front = (data//10)%10
        last = data%10
        if last >= front:
            pass
        else:
            return -1
        data = data//10
    return result



T = int(input())
for Count in range(T):
    N = int(input())
    List = list(map(int,input().split()))
    Answer_List = []
    for i in range(len(List)-1):
        for j in range(i+1,len(List)):
            Answer_List.append(List[i]*List[j])
    Answer = []
    for i in range(len(Answer_List)):
        result = danzo(Answer_List[i])
        Answer.append(result)
    print("#{} {}".format(Count+1,max(Answer+[-1])))
