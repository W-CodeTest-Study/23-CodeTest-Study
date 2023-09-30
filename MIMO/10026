import sys
from collections import deque

def bfs(a,b,result,maap,visited,p):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([a,b])
    visited[a][b] = p
    while(len(q)!=0):
        x, y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx< 0 or ddy < 0 or ddx >=n or ddy >=n:
                continue
            elif maap[ddx][ddy] == result and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = p
                q.append([ddx,ddy])

n = int(input())
board = []
green = []
boardvisited = [[0]* n for _ in range(n)]
greenvisited = [[0]* n for _ in range(n)]
boardcnt = {}
greencnt = {}
boardans = 0
greenans = 0
p = 0
for i in range(n):
    a = list(map(str,sys.stdin.readline().split()))
    cnt = []
    for j in range(len(a[0])):
        cnt.append(a[0][j])
    board.append(cnt)
for i in range(len(board)):
    tmp = []
    for j in range(len(board[0])):
        if board[i][j] == 'R' or board[i][j] == 'G':
            tmp.append('C')
        else:
            tmp.append('B')
    green.append(tmp)
for i in range(n):
    for j in range(n):
        p+=1
        if boardvisited[i][j] == 0:
            bfs(i,j,board[i][j],board, boardvisited,p)
        if greenvisited[i][j] == 0:
            bfs(i,j,green[i][j], green, greenvisited,p)
for i in range(n):
    for j in range(n):
        if boardvisited[i][j] not in boardcnt:
            boardcnt[boardvisited[i][j]] = 1
            boardans += 1
        if greenvisited[i][j] not in greencnt:
            greencnt[greenvisited[i][j]] = 1
            greenans += 1
print(boardans, greenans)
