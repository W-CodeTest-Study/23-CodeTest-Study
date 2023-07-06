# 프로그래머스 - 콜라츠 추측
def solution(num):
    answer = -1

    for i in range(500):
        if num == 1:
            answer = i
            break

        if num % 2 == 0: # 입력된 수가 짝수면 2로 나눔
            num = num / 2
        else: # 입력된 수가 홀수라면 3을 곱하고 1을 더함
            num = num * 3 + 1

    return answer