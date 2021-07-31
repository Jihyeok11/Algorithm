import sys
sys.stdin = open("2493in.txt",'r')

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().strip().split()))
answer = [0]
ba = [(0, li[0])]
for i in range(1, len(li)):
    if ba[0][1] < li[i]:
        ba = [(i, li[i])]
        answer.append(0)
    else:
        while ba:
            top = ba.pop()
            if top[1] > li[i]:
                answer.append(top[0] + 1)
                ba.append(top)
                ba.append((i, li[i]))
                break
print(*answer)