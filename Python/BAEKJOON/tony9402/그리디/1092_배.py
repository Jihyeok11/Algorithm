import sys
sys.stdin = open("1092in.txt", 'r')

n = int(sys.stdin.readline())
crane = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)
m = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)

# 옮겨 졌는지 확인을 위한 boxes 크기의 리스트를 만든다 
vi = list(True for _ in range(m))
position = list(0 for _ in range(n))
answer = 0
if boxes[0] > crane[0]:
    print(-1)
else:
    # 모든 화물을 옮길 때 까지(하나라도 vi에 True값이 있다면 while문 실행)
        for cont in range(len(crane)):
            # 각각의 컨테이너가 m의 위치까지 갈 때까지 실행
            while position[cont] < m:
                # 만약 옮길 수 있는 화물이 생긴다면 position[cont]위치에서 한 칸 움직이고 멈추게 된다.
                if crane[cont] >= boxes[position[cont]] and vi[position[cont]]:
                    vi[position[cont]] = False
                    break
                position[cont] += 1
        answer += 1
    print(answer)