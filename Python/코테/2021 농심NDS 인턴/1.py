import sys
sys.stdin = open("1in.txt",'r')

def solution(s):
    answer = 0
    baZ = True
    baA = True
    for word in s:
        if word == "z" and baZ:
            baZ = False
        elif word == "a" and not baZ:
            answer += 1
            baZ = True
        if word == "a" and baA:
            baA = False
        elif word == "z" and not baA:
            answer+= 1
            baA = True
    return answer

s = input()
print(solution(s))