from collections import deque


def solution(priorities, location):
    prior = deque(priorities)
    index = deque(list(i for i in range(len(priorities))))
    answers = []

    while len(prior) != 0:
        max_process = max(prior)
        one_prior = prior.popleft()
        one_index = index.popleft()
        if (one_prior == max_process):
            answers.append(one_index)
            continue
        else:
            prior.append(one_prior)
            index.append(one_index)

    answer = answers.index(location)+1
    return answer
