#문제 접근 : 처음에는 dfs로 풀어야 겠다는 생각을 하였다. 하지만, dfs로 구현을 해보니 갈림길에서의 길 구현이 원활하지 않아서 bfs로 풀어야 겠다 생각을 바꿨다. 그렇게 bfs로 풀어주고, visited 배열을 선언해서 방문을 확인해주면서 돌 때 효율성 검사에서 걸렸다. 그래서 visited 배열 확인을 빼주고 visited를 거리계산 하는 용도로 사용해 주었다
from collections import deque
def dfs(array,visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while(q):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx>=len(array) or ddy <0 or ddy >= len(array[0]):
                continue
            elif visited[ddx][ddy] != -1:
                continue
            elif array[ddx][ddy] == 0:
                continue
            else:
                q.append([ddx,ddy])
                visited[ddx][ddy] = visited[x][y] + 1

    return visited
def solution(maps):
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    answer = dfs(maps, visited)
    if answer[-1][-1] == 1:
        return -1
    else:
        return answer[-1][-1]