import sys
sys.stdin = open("1874in.txt",'r')

import sys
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().strip()))
ba = [1]
idx = 0
num = 1
ans = ["+"]
flag = 1
while idx < len(li):
    if not ba:
        ba.append(num+1)
        num += 1
        ans.append("+")
    elif ba[-1] < li[idx]:
        ans.append("+")
        ba.append(num+1)
        num += 1
    elif ba[-1] == li[idx]:
        ans.append("-")
        ba.pop()
        idx += 1
    elif ba[-1] > li[idx]:
        flag = 0
        break
if flag:
    for i in ans:
        print(i)
else:
    print("NO")