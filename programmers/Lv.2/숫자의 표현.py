'''
문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.

https://school.programmers.co.kr/learn/courses/30/lessons/12924?language=python3#
'''

def solution(n):
    # n일때는 무조건 +1이므로
    answer = 1
    # 예를 들어 15일 경우 1~8까지 반복
    for i in range(1, n // 2 + 1):
        stack = []
        # i ~ n+1 까지의 합 stack에 저장
        for j in range(i, n + 1):
            stack.append(j)
            # stack의 합이 n보다 크면 break
            if sum(stack) >= n:
                break
        # sum이 n 이면 answer +1 
        if sum(stack) == n:
            answer += 1
    return answer

'''
stack을 사용하지않고 합계를 이용한 코드 
'''
def solution(n):
    answer = 0
    # 1부터 n+1까지 반복
    for i in range(1, n+1):
        sum = 0
        # i부터 n+1까지 합
        for j in range(i, n+1):
            sum += j
            # sum이 n이면 answer +1 하고 break
            if sum == n:
                answer += 1
                break
            # sum이 n보다 크면 break
            elif sum > n:
                break
    return answer