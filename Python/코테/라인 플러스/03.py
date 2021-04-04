def solution(n):
    count = 0
    while n>=10:
        count += 1
        String = str(n)
        half = len(String)//2
        while String[half] == '0':
            half += 1
        front = String[:half]
        back = String[half:]
        n = int(front)+int(back)
    
    answer = [count,n]
    return answer

n = 73425
n = 100079
n = 9
result = [4,3]
result = [4, 8]
result = [0, 9]

solution(n)