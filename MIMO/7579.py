#7576과 완전 똑같은 문제 하나 다른점은 2차원 배열이 아니라 3차원 배열이라는 점이다.

import sys
from collections import deque
m,n,h  = map(int, sys.stdin.readline().split())
tomato = [[] for _ in range(h)]
dx = [0,-1,0,1]
dy = [-1,0,1,0]
dz = [-1,1] #3차원 배열이기 때문에 z축이 증가, 감소하는 것을 추가해 주었다.
dq = deque()
ans = 0
for j in range(h):
    for i in range(n):
        a = list(map(int, sys.stdin.readline().split()))
        tomato[j].append(a)
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                dq.append([k,i,j])
while(len(dq)!=0):
    print(tomato)
    a,b,c = dq.popleft()
    for k in range(4):
        if b + dx[k] >= 0 and b + dx[k] <= n-1 and c + dy[k] >= 0 and c + dy[k] <= m-1 and tomato[a][b+dx[k]][c+dy[k]]==0:
            tomato[a][b+dx[k]][c+dy[k]] = tomato[a][b][c] +1
            dq.append([a,b+dx[k],c+dy[k]])
    for k in range(2):  #z축에 대한 검사를 진행하면 된다
        if a + dz[k] >=0 and a + dz[k] <= h-1 and tomato[a+dz[k]][b][c] == 0:
            tomato[a+dz[k]][b][c] = tomato[a][b][c] + 1
            dq.append([a+dz[k],b,c])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                print(-1)
                quit()
        ans = max(ans, max(tomato[k][i]))
print(ans-1)