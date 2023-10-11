import sys
from collections import deque

input = sys.stdin.readline

# input
N, M = map(int, input().split())
maps = []

for _ in range(N):
  tmp_arr = []
  tmp_str = input()
  for char in tmp_str.rstrip():
    tmp_arr.append(int(char))
  maps.append(tmp_arr)

def bfs(maps):
  N = len(maps)
  M = len(maps[0])
  Q = deque([[0, 0, 0]])

  visited = [[[0,0] for _ in range(M)] for _ in range(N)]
  visited[0][0][0] = 1

  dxdy = [(1,0),(-1,0),(0,1),(0,-1)]

  while(Q):
    x, y, w = Q.popleft()

    if x == N-1 and y == M-1:
      return visited[x][y][w]

    for dx, dy in dxdy:
      # 범위 벗어남
      if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= M:
        continue

      # 벽이없어서 이동가능하고, 방문한 적이 없으면
      if maps[x+dx][y+dy] == 0 and visited[x+dx][y+dy][w] == 0:
        Q.append([x+dx,y+dy,w])
        visited[x+dx][y+dy][w] = visited[x][y][w] + 1
      # 벽이 있는데, 벽을 부순적이 없으면
      if maps[x+dx][y+dy] == 1 and w == 0:
        Q.append([x+dx,y+dy,w+1])
        visited[x+dx][y+dy][w+1] = visited[x][y][w] + 1

  return -1

print(bfs(maps))