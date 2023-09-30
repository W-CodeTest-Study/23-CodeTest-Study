import sys
sys.setrecursionlimit(10**9)

N,M,K = map(int,sys.stdin.readline().split())
count = {}
def dfs(a,b,cnt):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited[a][b] = cnt
    for i in range(4):
        ddx = a + dx[i]
        ddy = b + dy[i]
        if ddx <0 or ddy < 0 or ddx >=N or ddy >= M:
            continue
        elif board[ddx][ddy] == 1 and visited[ddx][ddy] ==0 :
            dfs(ddx,ddy,cnt)
        else:
            continue

board = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = -1
cnt = 0
for i in range(K):
    x,y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1
for i in range(N):
    for j in range(M):
        cnt +=1
        if board[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j,cnt)
            count[cnt] = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] != 0:
            count[visited[i][j]] +=1
print(max(list(count.values())))