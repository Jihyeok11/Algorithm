import sys
sys.stdin = open("7675in.txt",'r')

def Name(String,Length): # ['Annyung', 'Hasae', 'Yo!', 'LoL!']
    global flag
    if String[-1] == '!' or String[-1] == '?' or String[-1] == '.': # Flag 조건
        flag = 1
        if len(String)==1: # 한 글자면 
            return 0
        
        for i in range(len(String)-1):
            if i==0:
                if String[0].isnumeric() or String[0].islower():
                    return 0

            else:
                if String[0].isnumeric() or String[i].isupper() :
                    return 0
        return 1


    else: # 마지막 단어가 ?, ., ! 가 아닐 때
        for i in range(len(String)):
            if i ==0:
                if String[0].isnumeric() or String[0].islower():
                    return 0
            else:
                if String[i].isnumeric() or String[i].isupper():
                    return 0
        return 1


T = int(input())
for Count in range(T):
    print("#{} ".format(Count+1),end='')
    N = int(input())
    Str = list(map(str,input().split())) 
    total = 0
    flag = 0
    for String in Str:
        Len = len(String)
        total += Name(String,Len)
        if flag:
            print(total,end =' ')
            total = flag = 0
    print()
    