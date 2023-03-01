#문제 접근 : 단순 구현 문제였다. 톱니바퀴를 돌리는 것은 deque를 사용해서 popleft, appendleft를 이용해 구현하면 되겠다는 생각이 바로 들었지만, 주변 톱니바퀴의 상태를 확인해서 돌려야 할지 말지를 정해야하는 부분에서 좀 어려움을 겪었다. 톱니바퀴가 4개밖에 없어서 하나씩 해줘도 된다는 생각으로 전부 해주었는데, 좋지 않은 아이디어지만 문제를 해결해줄 수 있었다
import sys
from collections import deque
topni =[]
for i in range(4):  #입력을 받으면서 deque로 리스트에 저장한다
    cnt = deque()
    a = sys.stdin.readline().split()
    for j in range(len(a[0])):
        cnt.append(a[0][j])
    topni.append(cnt)
n = int(input())
for i in range(n):  
    a,b = map(int, sys.stdin.readline().split())
    command = []    #어떤 톱니바퀴를 어느 방향으로 돌려야 할지를 정하는 배열
    cnt = a-1   #배열은 0부터 시작하기 때문에 이에 맞게 변경
    if cnt == 0:    #0이면 왼쪽이 없으므로 올라가면서만 신경써주면 된다
        command.append([0,b])   #우선 첫번쨰 command를 넣어주고
        b = b*-1    #톱니바퀴의 방향을 바꿔야 하기 때문에 *-1을 해준다
        for j in range(3):  #뒤를 계속확인해주기 위해 3번만 돎
            if topni[j][2] == topni [j+1][6]:   #항상 다음 톱니바퀴의 6번째를 확인해주면 된다
                break
            else:
                command.append([j+1,b]) #서로 다르다면 돌려야 하므로 command 추가
                b = b*-1
    elif cnt == 1: #1과 2는 결이 같다. 각각 뒤와 앞에 1개씩 있으니 그걸 따로 조사하고 그 이후거를 또 따로 조사해준다
        command.append([1,b])
        b = b*-1
        if topni[0][2] != topni[1][6]:
            command.append([0,b])
        if topni[1][2] != topni[2][6]:
            command.append([2,b])
            b = b*-1
            if topni[2][2] != topni[3][6]:
                command.append([3,b])
    elif cnt == 2:
        command.append([2,b])
        b = b*-1
        if topni[2][2] != topni[3][6]:
            command.append([3,b])
        if topni[2][6] != topni[1][2]:
            command.append([1,b])
            b = b*-1
            if topni[0][2] != topni[1][6]:
                command.append([0,b])
    elif cnt == 3:
        command.append([3,b])
        b = b*-1
        for j in range(3,0,-1):
            if topni[j][6] == topni[j-1][2]:
                break
            else:
                command.append([j-1,b])
                b = b*-1
    for k in command:   #command배열에 담겨있는 인덱스들을 빼주면서 톱니바퀴를 돌려준다
        c,d = k
        if d == -1:
            out = topni[c].popleft()
            topni[c].append(out)
        elif d == 1:
            out = topni[c].pop()
            topni[c].appendleft(out)
answer = 0
n = 1
for i in range(4):
    if topni[i][0] == '1':
        answer += n
    n = n*2
print(answer)