import sys
sys.stdin = open("4008in.txt",'r')


def mycalc(a, b, i):
    if not i:
        return a + b
    elif i == 1:
        return a - b
    elif i == 2:
        return a * b
    # C, C++과의 차이로 //연산자가 버림이 아닌 내림을 해서 결과가 제대로 나오지 않았다.
    else:
        return int(a / b)
 
def dfs(x):
    global n
    if x > n - 2:
        result.append(temp[-1])
        return
    else:      
        for i in range(len(count)):
            if count[i]:
                temp.append(mycalc(temp[-1], nums[x+1], i))
                count[i] -= 1
                dfs(x+1)
                count[i] += 1
                temp.pop()
T = int(input())
for test in range(1, T+1):
    n = int(input())
    count = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    result = []
    temp = [nums[0]]
    dfs(0)
    result
    print('#{} {} {}'.format(test, max(result) , min(result)))