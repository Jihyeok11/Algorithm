def solution(heights):
    answer = [0]*len(heights)
    print(len(heights))
    for i in range(len(heights)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if heights[i]<heights[j]:
                answer[i]=j
                
    
    
    
    return answer

solution([6,9,5,7,4])