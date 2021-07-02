import sys
sys.stdin = open("10799in.txt",'r')

ba = sys.stdin.readline().strip()
cnt = 0 # 딱 대고 잇는 막대기
leg = 0 
answer = 0

while cnt < len(ba):
    if ba[cnt:cnt+2] == "()":
        answer += leg
        cnt += 2
    else:
        if ba[cnt] == "(":
            leg += 1
            answer += 1
        elif ba[cnt] == ")":
            leg = max(0,leg-1)
        cnt += 1
print(answer)
    