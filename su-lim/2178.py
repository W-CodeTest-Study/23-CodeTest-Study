# 백준 2178
# 문제접근 : 큐에는 접근할 칸의 위치를, 2차원 배열에는 시작점으로 부터의 거리를 저장한다.
#          시작점에서 상하좌우를 탐색하면서, 이동할 수 있는 칸이면 큐에 넣고, 큐에 있는 값을 기준으로
#          자신의 상하좌우를 탐색하면서 이동할 수 있는 칸이면 자신의 거리값 + 1로 저장을 한다.
#          더 이상 큐에 값이 들어오지 않으면 도착지점의 값을 출력한다.

# 입력값 => 거리에 따라 저장한 값
# 1 0 0     1 0 0
# 1 0 1  => 2 0 6
# 1 1 1     3 4 5

# 입력 및 값 초기화
import sys
from collections import deque
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int, input().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, input().strip())))

dx = [0,0,-1,1] # 상하좌우
dy = [1,-1,0,0]

# 1을 max 값으로 초기화, graph에는 시작점으로 부터의 거리를 저장
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      graph[i][j] = MAX

graph[0][0] = 1 # 시작 거리 1
q = deque([[0,0]]) # 시작 위치 큐에 삽입
while q:
  i, j = q.popleft()

  for k in range(len(dx)):
    kx, ky = i+dx[k], j+dy[k] # 상,하,좌,우에 대한 좌표
    if kx > -1 and ky > -1 and kx < N and ky < M: # 배열을 넘어선 범위가 아니면
      if graph[kx][ky] != 0: # 이동할 수 있는 칸이면
        origin = graph[kx][ky]
        graph[kx][ky] = min(graph[i][j] + 1, graph[kx][ky]) # 현재 위치에서 거리 1을 더한 값과 기존 값 중 작은 값을 넣음
        if origin != graph[kx][ky]: # 만약 기존 값이 변했다면, 큐에 넣음
          q.append([kx,ky])

# 도착 위치 값 출력
print(graph[N-1][M-1])