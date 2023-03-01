import sys
from collections import deque
m,n  = map(int, sys.stdin.readline().split())
tomato = []
dx = [0,-1,0,1]
dy = [-1,0,1,0]
dq = deque()    #bfs사용할 떄 popleft를 해줘야 하기 때문에 deque로 선언
ans = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    tomato.append(a)
for i in range(n):  #우선 배열을 다 뒤진 뒤에 1이 몇개인지 초기 세팅을 해준다.
    for j in range(m):
        if tomato[i][j] == 1:
            dq.append([i,j]) 
while(len(dq)!=0):  #deque가 빌때까지 while문 돈다
    a,b = dq.popleft()
    for k in range(4):  #deque에서 하나씩 빼서 범위가 넘어가지 않고, 0인 경우에만 표시를 해둔다.
        if a + dx[k] >= 0 and a + dx[k] <= n-1 and b + dy[k] >= 0 and b + dy[k] <= m-1 and tomato[a+dx[k]][b+dy[k]]==0:
            tomato[a+dx[k]][b+dy[k]] = tomato[a][b] +1  #이전 숫자에서 1을 추가해 해당 토마토가 언제 익었는 지를 나타내준다.
            dq.append([a+dx[k],b+dy[k]])
for i in range(n):  #배열을 돌면서 0이 있으면 -1을 출력하고 0이 없다면 max값을 저장해준다.
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            quit()
    ans = max(ans, max(tomato[i]))
print(ans-1)