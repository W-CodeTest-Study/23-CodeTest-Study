# 프로그래머스 - 단어 변환
# 알고리즘 - BFS

from collections import deque

# isSubOne(): 알파벳이 1개 차이나는 경우 1을 반환하는 함수
def isSubOne(begin, word):
    result = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            result += 1
    if result == 1:
        return 1
    else:
        return 0

def solution(begin, target, words):

    answer = 0

    visit = {}
    for word in words:
        visit[word] = 0

    # 큐가 빌 때까지 반복
    q = deque([(begin, 0)])
    while q:
        value, cnt = q.popleft()

        for word in words:
            # value와 word의 단어가 1개 차이나면서 방문한 적이 없는 경우
            if isSubOne(value, word) and not visit[word]:
                q.append((word,cnt+1))
                visit[word] = 1

                if word == target:
                    if answer == 0: # 초기값이면 현재값 저장
                        answer = cnt+1
                    else:
                        answer = min(answer, cnt+1)

    return answer