import sys
sys.stdin = open("4371in.txt",'r')

for Count in range(int(input())): # T회 실행
    List = []
    for _ in range(int(input())): # N회 실행, 코드를 줄이기 위해서 range안에 input()값을 바로 집어넣음
        List.append(int(input())-1) # N회 동안 (입력값-1)을 List 안에 집어넣는다.
    Answer = 0 # 정답이 될 배의 최소 수
    while any(List): # List값을 모두 0으로 될때까지 while을 돌린다.
        for i in range(1,len(List)): # 첫번째 값은 어차피 0이니 두번째 값부터 확인한다.
            if List[i]: # 만약 값이 0이 아니라면
                Answer += 1 # Answer 값을 1씩 올린다.
                A = List[i] 
                for j in range(i,len(List)): # i번째 값부터 끝까지 확인해서 A의 배수인 값들을 확인한다.
                    if not List[j]%A: # 나머지 값이 0이면 
                        List[j] = 0 # 그 값은 0이라고 한다
    print("#{} {}".format(Count+1,Answer)) # 출력값과 동일한 형식으로 출력한다.