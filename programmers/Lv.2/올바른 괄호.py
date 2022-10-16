'''
문제 설명
괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

제한사항
문자열 s의 길이 : 100,000 이하의 자연수
문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer = True
    # stack으로 담을 배열 
    arr = []
    for i in s:
        # i가 "("이면 arr에 "(" 추가
        if i == "(":
            arr.append(i)
            #그렇지 않을 때
        else: 
            # arr이 빈 배열이면 False 하고 break
            if arr == []:
                answer = False
                break
            # arr이 빈 배열이 아니면 pop()으로 마지막 index 제거 
            else: arr.pop()
    # 반복문이 끝나고 arr이 빈 배열이 아니면 False
    if arr != []:
        answer = False
    return answer