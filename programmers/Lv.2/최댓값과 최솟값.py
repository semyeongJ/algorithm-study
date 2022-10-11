'''
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

https://school.programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    s_list = s.split()
    str_to_int = []
    for i in range(len(s_list)):
        str_to_int.append(int(s_list[i]))
    s_max = max(str_to_int)
    s_min = min(str_to_int)
    answer =  str(s_min)+ ' ' + str(s_max)
    return answer

'''
아래는 다른 사람의 풀이
'''

def solution(s):
    # map에 int와 list를 넣으면 list의 모든 요소를 int로 변환 -> 그 다음 list를 사용해서 map의 결과를 다시 list에 담음
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))