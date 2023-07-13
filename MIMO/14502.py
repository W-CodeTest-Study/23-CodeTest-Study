import sys
from itertools import combinations
from collections import deque
import copy
def bfs(newlab):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    answer = 0
    visited = [[0 for _ in range(b)] for _ in range(a)]
    dq = deque()
    for i in range(a):
        for j in range(b):
            if newlab[i][j] == 2:
                dq.append([i,j])
    while(dq):
        x,y = dq.popleft()
        visited[x][y] = 1
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx >=a or ddy <0 or ddy >= b:
                continue
            elif newlab[ddx][ddy] == 1 or newlab[ddx][ddy] == 2:
                visited[ddx][ddy] = 1
                continue
            elif newlab[ddx][ddy] == 0 and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = 1
                newlab[ddx][ddy] = 2
                dq.append([ddx,ddy])
    for i in range(a):
        for j in range(b):
            if newlab[i][j] == 0:
                answer +=1
    safety.append(answer)    

a,b = map(int,sys.stdin.readline().split())
lab = []
zero = []
safety = []
for i in range(a):
    c = list(map(int,sys.stdin.readline().split()))
    lab.append(c)
for i in range(a):
    for j in range(b):
        if lab[i][j] == 0:
            zero.append([i,j])
nc3 = list(combinations(zero,3))
for i in nc3:
    cnt = copy.deepcopy(lab)
    cnt[i[0][0]][i[0][1]] = 1
    cnt[i[1][0]][i[1][1]] = 1
    cnt[i[2][0]][i[2][1]] = 1
    bfs(cnt)
    cnt[i[0][0]][i[0][1]] = 0
    cnt[i[1][0]][i[1][1]] = 0
    cnt[i[2][0]][i[2][1]] = 0
print(max(safety))