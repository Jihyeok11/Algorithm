import sys
sys.stdin = open("1003in.txt",'r')

n = int(sys.stdin.readline())
li = list(int(sys.stdin.readline()) for _ in range(n))
maxNum = max(li)
ba = [[1,0],[0,1]]
for i in range(2,maxNum+1):
    ba.append([ba[i-1][0]+ba[i-2][0], ba[i-1][1]+ba[i-2][1]])
for i in li:
    print(ba[i][0],ba[i][1])