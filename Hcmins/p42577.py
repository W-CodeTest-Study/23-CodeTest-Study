def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book)):
        # 중복되면 나머지 확인할 필요없음 -> 그만하기
        if (answer == False):
            break
        for j in range(i+1, len(phone_book)):
            # 이미 중복찾으면 그만하기
            if (answer == False):
                break

            for k in range(len(phone_book[i])):
                if (phone_book[i][k] != phone_book[j][k]):
                    break
                if (k == len(phone_book[i])-1):
                    answer = False

    return answer

# 수정후
# phone_book.sort() -> 문자형 오름차순이 된다. 이러면 반복문 여러번안써도됨


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = 0
        for j in range(len(phone_book[i])):
            if (phone_book[i][j] != phone_book[i+1][j]):
                break
            a += 1
        if (a == len(phone_book[i])):
            return False

    return True
