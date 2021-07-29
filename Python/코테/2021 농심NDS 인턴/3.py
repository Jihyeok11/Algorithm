import sys
sys.stdin = open("3in.txt",'r')

def solution(total_sp, skills):
    answer = []
    top = {} # {2: 1, 3: 1, 6: 3, 4: 3, 5: 3}
    bottom = [] # [2, 6, 4, 5]
    skill = {} # {1: 0, 2: 0, 3: 0, 6: 0, 4: 0, 5: 0}
    for a,b in skills:
        top[b] = a
        if not b in bottom:
            bottom.append(b)
        if a in bottom:
            bottom.remove(a)
        if not a in skill:
            skill[a] = 0
        if not b in skill:
            skill[b] = 0
    for i in bottom:
        skill[i] = 1
    while bottom:
        check = bottom.pop()
        try:
            skill[top[check]] += 1
            bottom.append(top[check])
        except:
            pass
    print(skill)
    skill = sorted(skill.items())
    total = 0
    for a,b in skill:
        total += b
    val = total_sp//total
    for a,b in skill:
        answer.append(b * val)
    return answer

total_sp = int(sys.stdin.readline())
li = []
for _ in range(5):
    a, b = map(int,input().split())
    li.append([a, b])
print(solution(total_sp, li))