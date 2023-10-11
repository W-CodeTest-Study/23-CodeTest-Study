from collections import deque
# input
N, M = map(int,input().split())

maps = []
for _ in range(N):
  maps.append(list(input()))

rx, ry, bx, by, ox, oy = 0,0,0,0,0,0
for i in range(N):
  for j in range(M):
    if maps[i][j] == "R":
      rx = i
      ry = j
    if maps[i][j] == "B":
      bx = i
      by = j
    if maps[i][j] == "O":
      ox = i
      oy = j

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def roll(x,y,i):
  nx, ny = x, y
  cnt = 0
  while not (maps[nx][ny] == "O" or maps[nx][ny] == "#"):
    nx+=dx[i]
    ny+=dy[i]
    cnt += 1
  if maps[nx][ny] == "O":
    return nx, ny, cnt
  return nx-dx[i], ny-dy[i], cnt-1

def bfs(rx,ry,bx,by):

  Q = deque([])
  Q.append([rx,ry,bx,by,0])
  visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  visited[rx][ry][bx][by] = 1

  while(Q):
    rx,ry,bx,by,cnt = Q.popleft()

    if cnt == 10: # 횟수 초과
      return -1

    cnt += 1
    for i in range(4):
      nrx, nry, rcnt = roll(rx,ry,i)
      nbx, nby, bcnt = roll(bx,by,i)

      if nbx == ox and nby == oy: # B가 통과
        continue

      if nrx == ox and nry == oy: # R 통과
        return cnt

      if nrx == nbx and nry == nby: # 제배치
        if rcnt > bcnt:
          nrx -= dx[i]
          nry -= dy[i]
        if bcnt > rcnt:
          nbx -= dx[i]
          nby -= dy[i]
      if visited[nrx][nry][nbx][nby] == 0:
        Q.append([nrx, nry, nbx, nby, cnt])
        visited[nrx][nry][nbx][nby] = 1

  return -1 # 방법을 찾지 못하면

# output
print(bfs(rx,ry,bx,by))