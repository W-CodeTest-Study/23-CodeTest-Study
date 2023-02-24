#문제 접근 : 시간 복잡도에 대한 고민을 살짝 했지만 더 좋은 방법이 생각나지 않아서 그냥 빡 구현을 선택했다. 빙고판이다 보니 가로검사,세로검사, 대각선검사가 필요했는데 모두 빡구현을 해주니 문제를 해결할 수 있었다.

import sys
bingo = []
ans = []
for i in range(5):
    a = list(map(int, sys.stdin.readline().split()))
    bingo.append(a)
for j in range(5):
    b = list(map(int, sys.stdin.readline().split()))
    ans+=b
for i in range(25):
    line = 0
    cnt = 0
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == ans[i]:
                bingo[j][k] = 0
    for j in range(5): #가로검사
        cnt = 0
        for k in range(5):
            if bingo[j][k] == 0:
                cnt +=1
        if cnt == 5:
            line +=1
    for j in range(5): #세로검사
        cnt = 0
        for k in range(5):
            if bingo[k][j] == 0:
                cnt +=1
        if cnt == 5:
            line +=1
    cnt = 0
    for j in range(5): #오른쪽아래 대각선 검사
        if bingo[j][j] == 0:
            cnt +=1
        if cnt == 5:
            line +=1
    cnt = 0
    for j in range(5):  #왼쪽아래 대각선 검사
        if bingo[j][4-j] == 0:
            cnt +=1
        if cnt == 5:
            line +=1
    if line >=3:
        print(i+1)
        break  

