def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        num = 0
        for j in range(1, i+1):
            if i % j == 0:
                num += 1
            if num > limit:
                num = power
                break
        answer += num
    return answer
