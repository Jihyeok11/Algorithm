Max = 0
def solution(numbers):
    global Max
    use_check = [True for _ in range(len(numbers))]
    use = [0 for _ in range(len(numbers))]
    def dfs(idx):
        global Max
        for i in range(len(numbers)):
            if use_check[i]:
                use_check[i] = False
                use[idx] = numbers[i]
                dfs(idx+1)
                use_check[i] = True
            if idx == len(numbers):
                Str= ''
                for k in range(len(use)):
                    Str += str(use[k])
                if Max < int(Str):
                    Max = int(Str)   
    dfs(0)
    print(Max)
    return
    
solution([3, 30, 34, 5, 9])