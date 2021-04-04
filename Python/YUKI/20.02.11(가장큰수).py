def solution(numbers):
    check =[ 0 for _ in range(len(numbers))]
    use_check = [True for _ in range(len(numbers))]
    Answer = []
    def dfs(idx):    
        for i in range(len(numbers)):
            if use_check[i]:
                use_check[i] = False
                check[idx] = numbers[i]
                dfs(idx + 1)
                use_check[i] = True

        if idx == len(a):
            for k in check:
                print(k, end ="")
            print()
            return

    dfs(numbers)
            


    answer = ''
    return answer


solution([3, 30, 34, 5, 9])