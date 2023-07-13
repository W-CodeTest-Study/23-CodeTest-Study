def checking(current, target, words, count, answers):

    if target not in words:
        return 0
    else:
        # 필요한 임시 words 생성
        temp_words = []
        for i in range(len(words)):
            temp_words.append(words[i])

        for i in range(len(words)):
            check = 0
            # 바꿀수있는 단어인지 확인(다른단어가 1개일때만)
            for j in range(len(current)):
                if (current[j] != words[i][j]):
                    check += 1
                if (check >= 2):
                    break
            # 바꿀수 있는 단어라면 바꾸고 확인
            if (check == 1):
                # target으로 바뀌면 그 수를 answers에 저장
                if (words[i] == target):
                    answers.append(count+1)
                # 아직도 다르면 계속 진행
                temp_words.remove(words[i])
                checking(words[i], target, temp_words, count+1, answers)

        return 0


def solution(begin, target, words):
    answers = []
    checking(begin, target, words, 0, answers)
    if (len(answers) == 0):
        return 0
    else:
        return min(answers)
