# 프로그래머스 - 타겟넘버
result = 0
def func(numbers, target, current):

    if not numbers:
        global result
        result += 1 if current == target else 0
        return

    num = numbers[0]
    func(numbers[1:], target, current+num)
    func(numbers[1:], target, current-num)

def solution(numbers, target):
    func(numbers,target,0)
    return result
