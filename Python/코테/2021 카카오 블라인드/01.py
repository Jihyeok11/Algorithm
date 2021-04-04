def solution(new_id):
    # 1단계, 2단계
    id2 = ''
    for i in new_id:
        if 64< ord(i) <91:
            id2 += chr(ord(i)+32)
        elif 47< ord(i) <58 or ord(i) == 45 or ord(i) == 46 or ord(i) == 95 or 96< ord(i)< 123:
            id2 += i
    
    # 3단계
    id3 = ''
    count = 0
    while count != len(id2):
        id3 += id2[count]
        if count != len(id2)-1 and id2[count]=='.' and id2[count+1]=='.':
            while count != len(id2)-1 and id2[count+1]=='.':
                count += 1
        count +=1

    # 4단계
    
    if id3:
        if id3[0]=='.':
            id3 = id3[1:]
        if id3 != '' and id3[-1]=='.':
            id3 = id3[:-1]

    # 5단계
    if not len(id3):
        id5 = 'a'
    else:
        id5 = id3
    # 6단계
    if len(id5)>=16:
        id6 = id5[:15]
        if id6[len(id6)-1]=='.':
            id6 = id6[:14]
    else:
        id6 = id5

    # 7단계
    if len(id6)<3:
        answer = id6
        while len(answer)<3:
            answer += id6[-1]
    else:
        answer = id6
    

    
    return answer

# new_id = "...!@BaT#*..y.abcdefghijklm"
# new_id = "z-+.^."
# new_id = "=.="
# new_id = "123_.def"
new_id = "abcdefghijklmn.p"

print(solution(new_id))
