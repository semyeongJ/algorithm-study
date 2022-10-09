'''
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

https://school.programmers.co.kr/learn/courses/30/lessons/12934#
'''

import math
def solution(n):
    answer = 0
    sqrt_n = int(math.sqrt(n))
    if (sqrt_n**2 == n):
        answer = (sqrt_n+1)**2
    else: answer = -1
    return answer

'''
아래는 더 짧은 코드로 수정
'''

import math
def solution(n):
    sqrt_n = int(math.sqrt(n))
    return (sqrt_n+1)**2 if sqrt_n**2 == n else -1