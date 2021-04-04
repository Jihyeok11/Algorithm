import sys
sys.stdin = open("in.txt",'r')

s = input()
# 여기서부터 

Leng = len(s)
if Leng%2:
    answer = s[Leng//2]
else:
    answer = s[Leng//2-1:Leng//2+1]

print(answer)



# 제출 코드

def solution(s):
    Leng = len(s) # 주어진 글자 길이를 측정
    if Leng%2: # 만약 길이 홀수이면
        answer = s[Leng//2] # 가운데 글자만 출력
    else: # 길이가 짝수이면
        answer = s[Leng//2-1:Leng//2+1] # 가운데 2개 범위를 측정 잘하여서 표시한다.
    return answer