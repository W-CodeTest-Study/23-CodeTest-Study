import itertools
def solution(numbers):
    answer = []
    result = list(itertools.combinations(numbers,2))
    for i in range(len(result)):
        answer.append(sum(result[i]))
    answer = set(answer)
    return sorted(list(answer))