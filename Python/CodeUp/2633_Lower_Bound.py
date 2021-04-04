import sys
sys.stdin = open("in.txt",'r')

n,k = map(int,input().split())
List = list(map(int,input().split()))
answer = 1
while answer-1<len(List):
    if List[answer-1]>=k:
        break
    answer += 1
print(answer)