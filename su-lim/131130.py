# 프로그래머스 - 혼자 놀기의 달인

def solution(cards):
    # 1. 초기값 입력
    visit = [0 for _ in range(len(cards))]
    path_list, path = [], []
    idx = 0

    # 2. 메인 로직
    while sum(visit) != len(cards): # 모두 방문할 때 까지 반복

        if visit[idx]: # 열었던 박스면
            if path: # 그동안의 path를 저장 후 비워줌
                path_list.append(path)
                path = []
            idx += 1
            continue
        path.append(cards[idx])
        visit[idx] = 1
        idx = cards[idx] - 1

    if path: # 패스에 남아있는게 있으면
        path_list.append(path)

    for i in range(len(path_list)):
        len(path_list[i])

    # 3. 결과 리턴

    # 1번 그룹에서 끝난 경우, 획득점수 0
    if len(path_list) < 2: return 0

    # 여러 그룹인 경우, 길이 내림차순으로 정렬 후 앞에서 부터 2개 그룹 곱하여 점수 계산
    path_list.sort(key=lambda x: -len(x))
    answer = len(path_list[0]) * len(path_list[1])
    return answer