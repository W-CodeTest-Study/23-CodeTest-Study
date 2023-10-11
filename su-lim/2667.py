import sys
from collections import deque

input = sys.stdin.readline

def bfs(maps, i, j):
  result = 0
  dxdy = [(0,1),(0,-1),(1,0),(-1,0)]

  maps[i][j] = 0
  Q = deque([[i,j]])

  while(Q):
    x, y = Q.popleft()
    result += 1

    for dx, dy in dxdy:
      if x+dx < 0 or x+dx >= len(maps) or y+dy < 0 or y+dy >= len(maps):
        continue
      if maps[x+dx][y+dy] == 1:
        maps[x+dx][y+dy] = 0
        Q.append([x+dx, y+dy])

  return result, maps


# 입력
N = int(input())
maps = []
result_arr = []

for _ in range(N):
  string = input()
  tmp_arr = []
  for char in string.strip():
    tmp_arr.append(int(char))
  maps.append(tmp_arr)

for i in range(N):
  for j in range(N):
    if maps[i][j] == 1:
      result, maps = bfs(maps, i, j)
      result_arr.append(result)

# print output
print(len(result_arr))
result_arr.sort()
for result in result_arr:
  print(result)