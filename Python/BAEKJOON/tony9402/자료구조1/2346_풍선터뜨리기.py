import sys
sys.stdin = open("2346in.txt",'r')

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
vi = list(True for _ in range(n))
vi[0] = False
answer = [1]
point = 0
while any(vi):
    cnt = li[point]
    step = 0
    while step != cnt:
        if cnt < 0:
            point -= 1
            if vi[point % n]:
                step -= 1

        else:
            point += 1
            if vi[point % n]:
                step += 1
    point %= n
    vi[point] = False
    answer.append(point+1)
print(*answer)