import sys
sys.stdin = open("2800in.txt",'r')

def words(cnt):
    global vi, answer
    if cnt == len(bracket):
        word = ""
        wordVi = list(True for _ in range(len(li)))
        for i in range(len(vi)):
            if not vi[i]:
                wordVi[bracket[i][0]] = False
                wordVi[bracket[i][1]] = False
        for i in range(len(li)):
            if wordVi[i]:
                word += li[i]
        if not word in answer:
            answer.append(word)
    else:
        vi.append(True)
        words(cnt+1)
        vi.pop()
        vi.append(False)
        words(cnt+1)
        vi.pop()

w = sys.stdin.readline().strip()
li = list(x for x in w)
ba = []
bracket = []
for i in range(len(li)):
    if li[i] == "(":
        ba.append(i)
    elif li[i] == ")":
        bracket.append((ba.pop(), i))
answer = []
vi = list()
words(0)
answer.sort()
answer.remove(w)
for word in answer:
    print(word)