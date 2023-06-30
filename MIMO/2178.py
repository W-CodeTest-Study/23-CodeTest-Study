#문제 접근 : DFS/BFS 많이 보던 유형이다. 근데 깊이 우선으로 풀어버리면 지나갔던곳을 다시 못지나가버리니까 지금 좌표 기준으로 안갔던곳을 한 번에 추가해 주어야 한다. 그래서 BFS로 풀어야 한다고 생각해서 접근해 주었다
import sys
from collections import deque

N,M  = map(int, sys.stdin.readline().split())   #입력
miro = []
visited = [[0]*M for _ in range(N)]

def bfs(a,b):   #bfs함수
    visited[a][b] = 1
    q = deque()
    q.append([a,b])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while(q):   #q가 빌 때까지 while문 돌기
        x,y = q.popleft()   #하나씩 확인
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx >= N or ddy < 0 or ddy >=M:
                continue
            elif miro[ddx][ddy] == '1' and visited[ddx][ddy] == 0:  #조건에 맞으면
                visited[ddx][ddy] = visited[x][y] + 1   #이전 값을 기준으로 다음 값 확인
                q.append([ddx,ddy]) #q에 추가


for i in range(N):
    cnt = []
    a = list(sys.stdin.readline().split())
    for j in range(M):
        cnt.append(a[0][j])
    miro.append(cnt)

bfs(0,0)
print(visited[N-1][M-1])