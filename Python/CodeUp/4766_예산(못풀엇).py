import sys
sys.stdin = open("in.txt",'r')

N = int(input())
List = list(map(int,input().split()))
bills = int(input())
List.sort()
for i in range(len(List)-1,-1,-1):
    stopPoint = List[i]
    result = 0
    for val in List:
        result += min(val,stopPoint)
    if result <= bills:
        break

count = 1   
while True:
    result = 0
    for val in List:
        result += min(val,stopPoint + count)
    if result>bills:
        break
    count += 1
print(count + stopPoint - 1)