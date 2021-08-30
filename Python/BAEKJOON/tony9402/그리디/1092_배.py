import sys
sys.stdin = open("1092in.txt", 'r')

n = int(sys.stdin.readline())
container = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)
m = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().strip().split())), key=lambda x:x, reverse=True)

# 옮겨 졌는지 확인을 위한 boxes 크기의 리스트를 만든다 
vi = list(True for _ in range(m))
position = list(0 for _ in range(n))
answer = 0
if boxes[0] > container[0]:
    print(-1)
else:
    while any(vi):
        idx = 0
        for cont in range(len(container)):
            for box in range(len(boxes)):
                while position[box] < m:
                    if container[cont] >= boxes[box] and vi[box]:
                        position[box] += 1
                        



        answer += 1
print(answer)