

def recur(numbers, target, count, comp_target) -> int:
    if (count == len(numbers)):
        if (comp_target == target):
            return 1
        return 0

    plus = comp_target+numbers[count]
    minus = comp_target-numbers[count]

    count += 1
    return recur(numbers, target, count, plus)+recur(numbers, target, count, minus)


def solution(numbers, target):
    return recur(numbers, target, 0, 0)
