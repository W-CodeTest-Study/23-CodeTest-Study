from collections import deque
import copy


def recur(k, dungeons, count, answers):
    # 임시 던전만들어서 빼서 돌리기
    end = 0  # 돌수없는 던전 수
    for i in range(len(dungeons)):
        dungeons_current = copy.deepcopy(dungeons)
        # 돌 수 있는 던전이면 그거 돌고 그 던전 없앤 후 다시 재귀돌림
        if (k >= dungeons[i][0]):
            dungeons_current.remove(dungeons[i])
            k_current = k-dungeons[i][1]
            recur(k_current, dungeons_current, count+1, answers)
        else:
            end += 1
    # 종료조건 : 더이상 돌수 있는 전선이 없을때 전선을 돈 횟수를 answers에 저장
    if (end == len(dungeons)):
        answers.append(count)
    return 0


def solution(k, dungeons):
    answers = [0]
    dungeons.sort(key=lambda x: -x[0])
    recur(k, dungeons, 0, answers)
    answer = max(answers)
    return answer
