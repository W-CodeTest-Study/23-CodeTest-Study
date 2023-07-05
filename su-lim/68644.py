#프로그래머스 - 두개 뽑아서 더하기
def solution(numbers):
    answer = []

    # numbers끼리 더하기
    for i in range(len(numbers)):
        for j in range(len(numbers[i+1:])):
            answer.append(numbers[i] + numbers[i+1:][j])

    # 중복 제거 후 정렬
    answer = sorted(list(set(answer)))
    return answer