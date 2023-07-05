# 프로그래머스 - 모의고사 (완전탐색)
def solution(answer):
    result = []

    # 초기값 설정
    score = [0,0,0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    # 문제 채점
    for i in range(len(answer)):
        if answer[i] == p1[i%len(p1)]:
            score[0] += 1
        if answer[i] == p2[i%len(p2)]:
            score[1] += 1
        if answer[i] == p3[i%len(p3)]:
            score[2] += 1

    # 많이 맞춘 사람 구하기
    for i in range(len(score)):
        if score[i] == max(score): result.append(i+1)
    return result