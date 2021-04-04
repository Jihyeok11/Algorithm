def bonae(u,v,Answer):
    left = right = 0
    right_is_bigger = False
    for i in u:
        if i=="(":
            left += 1
        elif i==")":
            right += 1
            if right >left:
                right_is_bigger = True

            if v : # v가 아직 있다면
                left = right = 0
                Answer = ""
                for i in v:
                    if i=="(":
                        left += 1
                    elif i==")":
                        right += 1
                    if left == right :
                        new_u = p[:i]
                        new_v = p[i:]
                        bonae(u,v,Answer)
                bonae(v)
        if right_is_bigger: # 올바른 괄호 문자열이면
            
            


def solution(p):
    left = right = 0
    Answer = ""
    for i in p:
        if i=="(":
            left += 1
        elif i==")":
            right += 1
        if left == right :
            u = p[:i]
            v = p[i:]
            bonae(u,v,Answer)
        break
    answer = ''
    return answer

p = "))(())(("
solution(p)