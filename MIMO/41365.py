#문제 접근 : 문제를 보고 순열조합으로 풀어야 겠다는 생각을 처음에는 했었는데, 그렇게 풀 수 없다는 것을 알고, bfs로 풀어야 겠다 생각했다. 앞에서부터 모든 경우의수를 따져가며 구해주어야 하기 때문에 bfs를 사용하며 문제를 해결해 주었다

from collections import deque

def solution(numbers, target):
    test = deque()  
    test.append([numbers[0],-numbers[0]])   #첫번째 들어갈 수 있는 경우의 수를 넣는다
    cnt = 0 #while문 안에서 배열의 위치를 정해주는 역할
    answer = 0
    while(test):    #test deque가 빌 때까지 while문을 돌아준다
        cnt += 1
        if cnt == len(numbers):     #위치가 배열의 길이와 같다면 break
            break
        tmp = []    #queue에 append 해주기 위한 배열 선언
        a = test.popleft()  #test에 있던 요소들 빼주기
        for i in a: #빼준 모든 요소를 돌면서 다음 요소를 +해준 값과 -해준 값을 append
            tmp.append(i + numbers[cnt])
            tmp.append(i - numbers[cnt])
        test.append(tmp)
    for i in test[0]:
        if i == target:
            answer+=1
    return answer