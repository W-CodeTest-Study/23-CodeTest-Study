# 설계과정 : 1번정답수 체크, 2번 정답수 체크, 3번 정답수 체크
# 이후에 가장높은 번수들을 찾아서 answer로 리턴

def solution(answers):
    num_correct = [0, 0, 0]
    num_1 = 0
    num_2 = 0
    num_3 = 0
    i = 0
    # 1번 정답수 체크
    for i in range(len(answers)):
        if (answers[i] == (i % 5++1)):
            num_correct[0] += 1
    # 2번 답 체크
    i = 0
    for i in range(len(answers)):
        answer_part2 = [1, 3, 4, 5]
        if (i % 2 != 0):
            if (answers[i] == answer_part2[(i//2) % 4]):
                num_correct[1] += 1
        else:
            if (answers[i] == 2):
                num_correct[1] += 1
    # 3번 답 체크
    i = 0
    for i in range(len(answers)):
        answer_part3 = [3, 1, 2, 4, 5]
        if (answers[i] == answer_part3[(i//2) % 5]):
            num_correct[2] += 1
    print(max(num_correct))
    i = 0
    answer = []
    for i in range(len(num_correct)):
        if (num_correct[i] == max(num_correct)):
            answer.append(i+1)

    return answer
