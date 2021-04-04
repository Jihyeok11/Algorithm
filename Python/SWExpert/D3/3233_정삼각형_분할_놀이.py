import sys
sys.stdin = open("3233in.txt",'r')

for Count in range(int(input())): # 주어지는 TestCase 개수만큼 전체 실행
    A,B = map(int,input().split()) # 입력값 A,B 입력
    quotient = A//B # A를 B로 나눈 값
    answer = 0 # 내가 원하는 정답
    for i in range(quotient):
        answer += 2*i+1 # 2X(층수)-1 은 다시쓰면 2x(층수-1)+1 과 같다.
    print("#{} {}".format(Count+1,answer)) # 정답 출력