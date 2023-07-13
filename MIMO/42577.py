def solution(phone_book):
    phone_book.sort()
    a=0
    for i in range(len(phone_book)-1):
        a=len(phone_book[i])
        if phone_book[i]==phone_book[i+1][:a]:
            return False
    return True