import sys
from collections import deque
input = sys.stdin.readline

def dfs(m,i,j):
  dxdy = [(0,1),(0,-1),(-1,0),(1,0)]
  Q = deque([[i,j]])
  while(Q):
    x, y = Q.popleft()
    for dx, dy in dxdy:
      if x+dx < 0 or x+dx >= len(m) or y+dy < 0 or y+dy >= len(m[0]):
        continue
      if m[x+dx][y+dy] == 1:
        m[x+dx][y+dy] = 0
        Q.append([x+dx,y+dy])
  return m

def search(m):
  result = 0

  for i in range(len(m)):
    for j in range(len(m[0])):
      if m[i][j] == 0:
        continue
      if m[i][j] == 1:
        m = dfs(m, i, j)
        result += 1

  return result

T = int(input())
maps = []
for _ in range(T):
  M, N, K = map(int, input().split())
  arr = [[0 for _ in range(N)] for _ in range(M)]
  for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1
  maps.append(arr)

for m in maps:
  print(search(m))