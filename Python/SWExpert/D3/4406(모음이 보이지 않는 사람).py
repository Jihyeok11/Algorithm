import sys
sys.stdin = open("4406in.txt",'r')

def AEIOU(String):
    vowel = ['a','e','i','o','u']
    result = ''
    for i in String:
        if not i in vowel:
            result += i
    return result

T = int(input())
for Count in range(T):
    String = input()
    answer = AEIOU(String)
    print("#{} {}".format(Count+1,answer))
