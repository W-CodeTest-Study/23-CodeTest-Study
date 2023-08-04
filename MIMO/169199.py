from collections import deque

def bfs(a,b,board,visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([a,b])
    visited[a][b] = 1
    while(q):
        x,y = q.popleft()
        if board[x][y] == 'G':
            return visited[x][y]
        for i in range(4):
            s, t = x,y
            while True:
                s, t = s + dx[i], t + dy[i]
                if s < 0 or t < 0 or s>=len(board) or t>=len(board[0]):
                    s -= dx[i]
                    t -= dy[i]
                    break
                elif board[s][t] == "D":
                    s -= dx[i]
                    t -= dy[i]
                    break
            if not visited[s][t]:
                visited[s][t] = visited[x][y] + 1
                q.append([s,t])
def solution(board):
    game = []
    visited = []
    answer = -1
    for i in range(len(board)):
        cnt = []
        cntvisited = []
        for j in range(len(board[i])):
            cnt.append(board[i][j])
            cntvisited.append(0)
        game.append(cnt)
        visited.append(cntvisited)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                answer = bfs(i,j,board,visited)
    if answer == None:
        return -1
    else:
        return answer-1