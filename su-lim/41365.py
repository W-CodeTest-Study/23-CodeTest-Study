# 프로그래머스 41365 타겟 넘버
answer = 0
def calc(numbers, result, target):
    if not numbers:
        if result == target:
            global answer
            answer+= 1
        return 0
    cur = numbers[0]
    calc(numbers[1:], result+cur, target)
    calc(numbers[1:], result-cur, target)

def solution(numbers, target):
    global answer
    calc(numbers, 0, target)
    return answer

# 예전에 풀이 보고 짠 코드, 위에 코드가 더 빠름
# _target = 0

# def dfs(numbers, mynum, op):
#     global _target

#     if op:
#         mynum += numbers.pop()
#     else:
#         mynum -= numbers.pop()
#     if not numbers:
#         if mynum == _target:
#             return 1
#         else:
#             return 0

#     return dfs(numbers.copy(), mynum, 1) + dfs(numbers.copy(), mynum, 0)

# def solution(numbers, target):
#     answer = 0

#     global _target
#     _target = target

#     numbers.reverse()
#     mynum = 0
#     answer = dfs(numbers.copy(), mynum, 1) + dfs(numbers.copy(), mynum, 0)

#     return answer