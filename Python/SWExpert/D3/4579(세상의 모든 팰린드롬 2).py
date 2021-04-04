import sys
sys.stdin = open("4579in.txt",'r')


for Count in range(int(input())):
    Name = input()
    flag = 1
    for i in range(len(Name)):
        First = Name[i]
        Last = Name[-(i+1)]
        if First == '*' or Last == '*':
            break
        elif First != Last:
            flag = 0
            break

    if flag:
        print("#{} Exist".format(Count+1))
    else:
        print("#{} Not exist".format(Count+1))
