import sys
sys.stdin = open("2816in.txt",'r')

n = int(sys.stdin.readline())
myList = list( sys.stdin.readline().strip() for _ in range(n))
index1 = myList.index("KBS1")
index2 = myList.index("KBS2")
if index1 > index2:
    index2 += 1
answer = "1"*index1+"4"*index1 
answer += "1"*index2+"4"*(index2-1)
print(answer)