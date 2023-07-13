
# target_group은 열었는지(1),안열었는지(0)를 담아눈 배열
# num: 총 사이클의 개수(같은 그룹의 개수)
def recur(cards, start, target_group, num):
    next_open_index = cards[start]-1  # 다음에 열 인덱스
    # 안열려있으면 열었다는 표시해주고
    if (target_group[next_open_index] == 0):
        target_group[next_open_index] = 1
        num += 1
        return recur(cards, next_open_index, target_group, num)
    # 열러있는거면 그만하고 그룹의 개수를 반환
    else:
        return num


def solution(cards):
    points = [0]  # 라운드2가 안도는 경우에는 points에 안담기기때문에 0 넣어두기

    for i in range(len(cards)):
        group = [0 for i in range(len(cards))]
        round_1 = recur(cards, i, group, 0)  # 첫번째 그룹의 개수
        # 현재 1라운드돌리고 group은 1라운드 그룹들이 1로 차있는 상태
        for j in range(i+1, len(cards)):
            # 어차피 1라운드에 같은 소속은 같은 그룹만 나오니까 2라운드에 돌릴필요없음
            if (group[j] == 1):
                continue
            # 1라운드때 같은 그룹이 아닌 애들로 돌려서 그 그룹수 확인
            round_2 = recur(cards, j, group, 0)
            point = round_1 * round_2
            points.append(point)
        # round별 그룹 수 초기화 후 반복진행
        round_2 = 0
        round_1 = 0
    answer = max(points)
    return answer

# 느낌 점 : 수진이처럼 임의로 선택해서 나온 그룹을 cards에서 빼고 그룹들을 리스트에 넣어서 그룹의 개수를 기준으로
# 내림차순 정렬후 앞에 요소 2개를 곱하는 방법이 훨씬 나은것 같음

# 또는 유니온-파인드도 이용해보기
