#문제 접근 : 문자열에 대한 처리만 잘 해주면 수월하게 풀 수 있는 문제다

def solution(book_time):
    book_time = sorted(book_time, key = lambda x:[x[0],x[1]])   #들어오는 배열을 정렬 해준다
    book = []   #문자열 시간으로 되어 있는 배열을 숫자로 변경해서 넣어주기 위한 배열 선언
    for i in book_time: #for문을 돌면서 문자열 시간으로 되어있는 숫자들을 전부 분 단위로 바꾸어서 배열에 저장한다
        a = int(i[0][0:2]) * 60 + int(i[0][3:5])
        b = int(i[1][0:2]) * 60 + int(i[1][3:5])
        book.append([a,b])
    room = []   #방이 몇개 필요한지 계산해주기 위해 배열을 선언해준다
    room.append(book[0][1] + 10)    #첫번째 인덱스를 빼서 room에 넣어준다
    book.pop(0)
    for i in range(len(book)):  #for문을 돌면서 빈 방이 나가는 방이 있으면 교체를 해주는데 status를 통해 상태를 점검한다.
        status = 0
        for j in range(len(room)):
            if book[i][0] >= room[j] and status == 0:
                room[j] = book[i][1] + 10
                status = 1
        if status == 0:
            room.append(book[i][1] + 10)
    return len(room)