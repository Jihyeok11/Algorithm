def solution(s):
    answer = ""
    # A = "12345"
    # cnt = 0
    # while A:
    #     A = A[-len(A)+3:]
    #     print(A)
    #     cnt += 1
    while s:
        if s[0].isdigit():
            answer += s[0]
            s = s[-len(s)+1:]
        else:
            if s[0]=="z":
                answer += "0"
                s = s[4:]
            elif s[0]=="o":
                answer += "1"
                s = s[3:]
            elif s[0]=="t":
                if s[1]=="w":
                    answer += "2"
                    s = s[3:]
                elif s[1] == "h":
                    answer += "3"
                    s = s[3:]
            elif s[0] =="f":
                if s[1] == "o":
                    answer += "4"
                    s = s[3:]
                elif s[1] == "i":
                    answer += "5"
                    s = s[4:]
            elif s[0] == "s":
                if s[1] == "i":
                    answer += "6"
                    s = s[3:]
                elif s[1]=="e":
                    answer += "7"
                    s = s[5:]
            elif s[0] == "e":
                answer += "8"
                s = s[5:]
            elif s[0]=="n":
                answer += "9"
                s = s[4:]
            
    return answer


solution("onetwothreefourfivesixseveneightninezero")
#"one4seveneight"	1478