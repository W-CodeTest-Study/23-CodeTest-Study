#문제 접근 : 어려운 알고리즘이 사용된 것이 아니라 문제에서 주어진 대로 구현하면 되는 문제였다. 어렵다고 느꼈던 부분은 0이 1사이에 막혀 있는지 확인하는 부분이ㅇ였는데, Status를 사용해서 이를 해결해 주었다.

import sys

m,n = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
world = [[0]*n for _ in range(m)]
status = True   #1로 둘러쌓여 있으면 status를 False로 바꾼다
answer = 0
for i in range(n):  #배열 생성
    for j in range(m-1, m-1-a[i],-1):
        world[j][i] = 1
for i in range(m):
    cnt = 0
    status = True
    for j in range(n-1):
        if world[i][j] == 1 and world[i][j+1] == 0: #현재 배열값이1, 다음 배열값이 0 즉 둘러쌓여있을 경우 status 변경
            status = False
        elif status == False and world[i][j] == 0 and world[i][j+1] == 1:   #현재 배열값0, 다음 배열값 1, 즉 다시 막힐 경우 status 변경
            cnt+=1
            status = True
            answer += cnt
            cnt = 0
        elif world[i][j] == 0 and status == False:  #단순히 0이면 cnt만 증가시켜준다.
            cnt+=1
print(answer)