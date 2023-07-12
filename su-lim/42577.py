# 프로그래머스 - 전화번호 목록
def solution(phone_book):
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
            return False
    return True