import sys
sys.stdin = open("1918in.txt",'r')

words = list(x for x in sys.stdin.readline().strip())
stack = []
ans = ""
for w in words:
    if w.isalpha():
        ans += w
    else:
        if (w == "+" or w == "-"):
            while stack and (stack[-1] != "("):
                ans += stack.pop()
            stack.append(w)
        elif (w == "*" or w == "/"):
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                ans += stack.pop()
            stack.append(w)
        elif w == "(":
            stack.append(w)
        elif w == ")":
            while stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
while stack:
    ans += stack.pop()
print(ans)