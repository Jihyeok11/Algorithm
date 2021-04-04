N = int(input())
Answer = [ N for _ in range(N+2)]
Answer[N] = 0

def MO(N):
    for i in range(N,0,-1):
            
        Answer[i] = min(Answer[i] , Answer[i+1] +1)

        if i%2 == 0:
            Answer[i//2] = min(Answer[i//2+1]+1, Answer[i]+1, Answer[i//2]) # 1만뺀거, 2로 나눈거, 원래 자기 값
        if i%3 == 0:
            Answer[i//3] = min(Answer[i//3+1]+1, Answer[i]+1, Answer[i//3])

MO(N)
print(Answer[1])