import sys
from collections import deque

def search(arr):
  # 맨 처음 1들을 큐에 넣음
  Q = deque([])
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == 1:
        Q.append([i,j])

  dxdy = [(0,1),(0,-1),(1,0),(-1,0)]

  while(Q):
    x, y = Q.popleft()

    for dx, dy in dxdy:
      if x+dx < 0 or x+dx >= len(arr) or y+dy < 0 or y+dy >= len(arr[0]):
        continue
      if arr[x+dx][y+dy] == 0:
        arr[x+dx][y+dy] = arr[x][y] + 1
        Q.append([x+dx,y+dy])
  return arr

# 입력
input = sys.stdin.readline
M, N = map(int, input().split())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())))

arr = search(arr)

day = 0
for row in arr:
  if 0 in row:
    print(-1)
    exit(0)
  if max(row) > day:
    day = max(row)
print(day-1)