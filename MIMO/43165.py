from collections import deque

def solution(numbers, target):
    test = deque()
    test.append([numbers[0],-numbers[0]])
    cnt = 0
    answer = 0
    while(test):
        cnt += 1
        if cnt == len(numbers):
            break
        tmp = []
        a = test.popleft()
        for i in a:
            tmp.append(i + numbers[cnt])
            tmp.append(i - numbers[cnt])
        test.append(tmp)
    for i in test[0]:
        if i == target:
            answer+=1
    return answer