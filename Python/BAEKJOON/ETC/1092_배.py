import sys
sys.stdin = open("1092in.txt", 'r')

n = int(sys.stdin.readline())
cranes = sorted(list(map(int ,sys.stdin.readline().split())), key=lambda x:-x)
m = int(sys.stdin.readline())
boxes = sorted(list(map(int ,sys.stdin.readline().split())), key=lambda x:-x)

answer = 0 
vi = list(True for _ in range(m))
crane_position = list(0 for _ in range(n))
while any(vi):
    answer += 1
    for crane in range(len(cranes)):
        while True:
            while crane_position[crane] < m and (not vi[crane_position[crane]]) :
                crane_position[crane] += 1
            if crane_position[crane] == m:
                break
            if boxes[crane_position[crane]] <= cranes[crane]:
                break
            else:
                crane_position[crane] += 1
        if crane_position[crane] == m:
            continue
        vi[crane_position[crane]] = False

print(answer)