#문제 접근 : 문제를 보고 알고리즘을 써야겠다는 생각 보다는 예외 사항 빠뜨리지 말고 구현을 잘 해야겠다는 생각을 했다. 우선 글자가 1개 차이나면 비슷한 단어로 봐야 하기 떄문에 맨 처음에 길이 비교를 해준 뒤 1개 읻상 차이나면 continue해주고, 1개 이하로 차이가 나면 부족한 단어에 0이라는 들어오지 않을 input을 더해 주어 비교를 진행했다. 0을 넣어주지 않으면 remove하고 나서의 판별 값이 달라질 수 있었기 때문에 두 문자열의 자리수를 맞춰준 뒤에 판별을 진행했다

n = int(input())
compare = input()
answer = 0
for i in range(n-1):
    b = input()
    tempcompare = compare #임시 문자열 선언
    if abs(len(compare) - len(b)) > 1: #1 넘어가면 continue
        continue
    elif len(compare) > len(b): #문자열 길이 맞추기
        b += '0'
    elif len(compare) < len(b): #문자열 길이 맞추기
        tempcompare += '0'
    comparearr = sorted(list(tempcompare))
    barr = sorted(list(b)) #str 배열로 선언, 사실 정렬은 해줄필요 x
    for j in comparearr: #comparearr돌면서 있는 단어들 삭제
        if j in barr:
            barr.remove(j)
    if len(barr) == 0 or len(barr) == 1:
        answer+=1
print(answer)