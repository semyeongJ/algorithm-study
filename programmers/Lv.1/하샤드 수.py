'''
문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

https://school.programmers.co.kr/learn/courses/30/lessons/12947
'''

def solution(x):
    x_srt = str(x)
    sum = 0
    # 자릿수 더하기
    for i in range(len(x_srt)):
        sum += int(x_srt[i])
    # x%sum == 0 이면 True 반환, 그렇지 않으면 False 반환
    return True if x%sum == 0 else False