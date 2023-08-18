def solution(k, m, score):
    score = sorted(score, reverse = True)
    answer = 0
    cnt = []
    for i in range(len(score)):
        if len(cnt) == m:
            answer += (cnt[-1] * m)
            cnt = []
            cnt.append(score[i])
        else:
            cnt.append(score[i])
    if len(cnt) == m:
        answer += (cnt[-1] * m)
    return answer