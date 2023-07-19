from collections import deque


def solution(priorities, location):
    prior = deque(priorities)  # 우선순위 큐
    index = deque(list(i for i in range(len(priorities))))  # 프로세스의 index 큐
    answers = []

    while len(prior) != 0:
        max_process = max(prior)
        one_prior = prior.popleft()
        one_index = index.popleft()
        # 가장 큰 우선순위이면 pop해주고 그 인덱스를 answers에 저장
        if (one_prior == max_process):
            answers.append(one_index)
            continue
        # 더 큰 우선순위가 있으면 다시 큐에 넣기
        else:
            prior.append(one_prior)
            index.append(one_index)
    # 현재 먼저 실행된(pop된) 프로세스 순으로 answers index가 담겨있으니까 원하는 index의 순서를 확인해서 return
    answer = answers.index(location)+1
    return answer
