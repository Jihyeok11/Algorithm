import sys
sys.stdin = open("1918in.txt",'r')

def bracket():
    global idx
    
    alpha = []
    sachic = []
    while True:
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
            word = alpha.pop(0)
            for i in range(len(sachic)):
                word += alpha[i] + sachic[i]
            return word
        elif words[idx] == "(":
            alpha.append(bracket())

words = list(x for x in sys.stdin.readline().strip())
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
ans = alpha.pop(0)
for i in range(len(alpha)):
    ans += alpha[i] + sachic[i]
print(ans)