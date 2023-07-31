def recur(n, current, target, answer):  # n:남은 수,current:현재 위치, target:이동한 위치, answer:경로저장용
    middle = 6-current-target  # 중간에 있는 애
    if (n == 1):
        answer.append([current, target])  # 옮긴거 저장
    if (n > 1):
        recur(n-1, current, middle, answer)  # 아래집합들 중간에 넣고
        recur(1, current, target, answer)  # 맨아래를 target으로 옮기고
        recur(n-1, middle, target, answer)  # 중간에 있는 아래집합을 다시 target으로

    return 0


def solution(n):
    answer = []
    recur(n, 1, 3, answer)
    print(answer)

    return answer
