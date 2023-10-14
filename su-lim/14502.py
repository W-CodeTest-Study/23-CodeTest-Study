from collections import deque
import copy

# 바이러스 퍼트리기
def virus():
  maps_copy = copy.deepcopy(maps)
  # maps_copy = [ i[:] for i in maps]

  Q = deque()
  dxdy = [(0,1),(0,-1),(1,0),(-1,0)]
  visit = [[0]*M for _ in range(N)]

  # 모든 2를 큐에 넣음
  for x in range(N):
    for y in range(M):
      if maps_copy[x][y] == 2:
        Q.append([x, y])
        visit[x][y] = 1

  # 바이러스 퍼짐
  while Q:
    x, y = Q.popleft()
    for dx,dy in dxdy:
      if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= M:
        continue
      if maps_copy[x+dx][y+dy] != 1 and visit[x+dx][y+dy] == 0:
        maps_copy[x+dx][y+dy] = 2
        Q.append([x+dx, y+dy])
        visit[x+dx][y+dy] = 1

  # 안전영역 구하기
  global MAX
  safe_area = 0
  for x in range(N):
    for y in range(M):
      if maps_copy[x][y] == 0:
        safe_area += 1
  MAX = max(safe_area, MAX)

# 벽 세울 위치 재귀
def search(cnt):

  if cnt == 3:
    virus() # 벽 세운 후 안전 영역 구하고, max값 업데이트
    return
  for i in range(N):
    for j in range(M):
      if maps[i][j] == 0:
        maps[i][j] = 1
        search(cnt+1)
        maps[i][j] = 0

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
MAX = 0
search(0)
print(MAX)