import sys
sys.stdin = open("2529in.txt",'r')

n = int(sys.stdin.readline())
li = list(sys.stdin.readline().split())
myList = []
vi = [True]*10
def makeList(List,n):
    if len(List)>=2:
        idx = len(List)-2
        if li[idx] == ">":
            if List[idx] < List[idx+1]:
                return
        elif li[idx]=="<":
            if List[idx] > List[idx+1]:
                return
    if len(List)==(n+1):
            myList.append(List)
            return
    for i in range(10):
        if vi[i]:
            vi[i] = False
            makeList(List+[i],n)
            vi[i] = True
makeList([],n)
Max = ""
for i in myList[-1]:
    Max += str(i)
Min = ""
for i in myList[0]:
    Min += str(i)
print(Max)
print(Min)