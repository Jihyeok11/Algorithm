def lenString(brick,s):
    my_string = {}
    brick += 1
    Answer = ''

    List = []
    for i in range(0,len(s),brick):
        A = s[i:i+brick]
        List.append(A)
    # ['a','a','b','b','a','c','c','c']
    for i in range(len(List)):
        A = List[i]
        cnt = 1
        start = i
        while start+1<len(List) and A == List[start+1]:
            start += 1
            cnt += 1
            List[start] = 0
        
        if List[i] and cnt != 1:
            Answer += str(cnt)+A
        elif List[i]:
            Answer += A

        
    return len(Answer)


def solution(s):
    Min = len(s)
    for i in range(len(s)):
        total_length = lenString(i,s) # brick 크기는 i+1이여야한다.
        if Min>total_length:
            Min = total_length
    answer = Min
    print(answer)
    return answer


s = "aabbaccc"
7
# s = "ababcdcdababcdcd" 2ababcdcd
9
# s = "abcabcdede" 2abcdede
8
# s = "abcabcabcabcdededededede" 2abcabc2dedede
14
# s = "xababcdcdababcdcd" x4ababcdcd
17
s = "abcabcabcabcdededededede"
solution(s)

# 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 
# 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다.
#  다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며,
#   이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.