import sys
sys.stdin = open("9012in.txt",'r')

import sys
n = int(sys.stdin.readline())
for _ in range(n):
    sentence = sys.stdin.readline().rstrip()
    flag = 1
    check=[]
    for i in sentence:
        if i=="(":
            check.append(i)
        elif i==")":
            if check and check.pop() =="(":
                pass
            else:
                flag = 0
                break
    if (not check) and flag:
        print("YES")
    else:
        print("NO")