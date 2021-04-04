import sys
sys.stdin = open("5658in.txt",'r')

T = int(input())
def Count_Max(i):
    global Int,Answer 
    Int1 = Int[i:N//4+i]
    if not int(Int1,16) in Answer:
        Answer.append(int(Int1,16))
    Int2 = Int[N//4 +i: N//2+i]
    if not int(Int2,16) in Answer:
        Answer.append(int(Int2,16))
    Int3 = Int[N//2 +i: (3 * N)//4+i]
    if not int(Int3,16) in Answer:
        Answer.append(int(Int3,16))
    Int4 = Int[-N//4+i:] + Int[:i]
    if not int(Int4,16) in Answer:
        Answer.append(int(Int4,16))

    

for Count in range(T):
    print("#{0} ".format(Count+1),end = '')
    N,M = map(int,input().split())
    Int = input()
    Answer = []
    for i in range(N//4):
        Count_Max(i)
    Answer.sort()
    print(Answer[-M])

