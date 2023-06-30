#문제 접근 : 전형적인 bfs문제이다. 다만, 마지막 조건을 보지 못해서 좀 해맸다
import sys
from collections import deque

def bfs(a,b):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([a,b])
    while(q):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx >=N or ddy < 0 or ddy >= M:
                continue
            elif route[ddx][ddy] == 1 and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = visited[x][y] + 1
                q.append([ddx,ddy])


N,M = map(int,sys.stdin.readline().split())
route = [[] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    for j in a:
        route[i].append(j)
for i in range(N):
    for j in range(M):
        if route[i][j] == 2:
            bfs(i,j)
for i in range(N):  #마지막 조건에서 갈수 잇는 곳인데 도달하지 못하면 -1로 표시하라 하였으므로 해당 조건에 맞춰준다.
    for j in range(M):
        if route[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
for i in range(N):
    print(*visited[i])