import sys
sys.stdin = open("2504in.txt",'r')

def bracket():
    ba = []
    for word in li:
        try:
            if word == "(":
                ba.append("(")
            elif word == "[":
                ba.append("[")
            elif word == ")":
                tp = 0
                while True:
                    last = ba.pop()
                    if last == "(":
                        ba.append(max(2,2 * tp))
                        break
                    elif last == "[":
                        return 0
                    else:
                        tp += last
            elif word == "]":
                tp = 0
                while True:
                    last = ba.pop()
                    if last == "[":
                        ba.append(max(3,3 * tp))
                        break
                    elif last == "(":
                        return 0
                    else:
                        tp += last
        except:
            return 0
    try:
        return sum(ba)
    except:
        return 0
                
li = list(x for x in sys.stdin.readline().strip())
print(bracket())