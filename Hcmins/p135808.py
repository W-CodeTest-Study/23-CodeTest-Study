def solution(k, m, score):
    answer = 0
    score.sort()
    n = len(score)//m
    while n:
        for i in range(m):
            apple = score.pop()
            if apple < k:
                k = apple
        answer += k*m
        n -= 1
    return answer
