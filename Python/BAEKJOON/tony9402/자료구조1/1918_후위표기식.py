import sys
sys.stdin = open("1918in.txt",'r')

def bracket():
    global idx
    
    alpha = []
    sachic = []
    while idx < len(words):
        idx += 1
        if words[idx].isalpha():
            alpha.append(words[idx])
        elif words[idx] == "+" or words[idx] == "-":
            sachic.append(words[idx])
        elif words[idx] == "*" or words[idx] == "/":
            if words[idx+1].isalpha():
                alpha.append( alpha.pop() + words[idx+1] + words[idx])
                idx += 1
            elif words[idx+1] == "(":
                tp = words[idx]
                idx += 1
                alpha.append(alpha.pop() + bracket() + tp)
        elif words[idx] == ")":
            if alpha:
                word = alpha.pop(0)
                for i in range(len(sachic)):
                    word += alpha[i] + sachic[i]
                return word
            else:
                return ""
        elif words[idx] == "(":
            alpha.append(bracket())

words = list(x for x in input())
idx = 0
alpha = []
sachic = []
while idx < len(words):
    if words[idx].isalpha():
        alpha.append(words[idx])
    elif words[idx] == "+" or words[idx] == "-":
        sachic.append(words[idx])
    elif words[idx] == "*" or words[idx] == "/":
        if words[idx+1].isalpha():
            alpha.append(alpha.pop() + words[idx+1] + words[idx])
        elif words[idx+1] == "(":
            tp = words[idx]
            idx += 1
            alpha.append(alpha.pop() + bracket() + tp)
        idx += 1
    elif words[idx] == "(":
        alpha.append(bracket())
    idx += 1
if alpha:
    ans = alpha.pop(0)
    for i in range(len(alpha)):
        ans += alpha[i] + sachic[i]
    print(ans)
else:
    print()