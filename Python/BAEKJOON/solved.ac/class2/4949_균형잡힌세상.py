import sys
sys.stdin = open("4949in.txt",'r')

import sys
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence==".":
        break
    flag = 1
    check=[]
    for i in sentence:
        if i=="[":
            check.append(i)
        elif i=="]":
            if check and  check.pop() == "[":
                pass
            else:
                flag = 0
                break
        elif i=="(":
            check.append(i)
        elif i==")":
            if check and check.pop() =="(":
                pass
            else:
                flag = 0
                break
    if (not check) and flag:
        print("yes")
    else:
        print("no")