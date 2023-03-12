#문제 접근 : 전형적인 dfs문제이다. 배열을 어떻게 돌지에 대한 것은 확실하게 잡아 놨지만 days를 처리하지 못해 시간이 좀 걸렸다. 결국에는 dfs를 재귀로 풀기 보다는 while문을 사용해서 bfs로 푸는 방법을 선택하였다

import sys
from collections import deque
sys.setrecursionlimit(10**5)
def solution(maps):
    def dfs(n,m,visited):
        dx = [-1,0,1,0] #방향 설정
        dy = [0,-1,0,1]
        visited[n][m] = 1   #visited배열에 등록
        q = deque()
        q.append([n,m]) #큐에 돌아다녀야 하는 배열 추가
        days = 0
        while(q):
            a,b = q.popleft()   #하나씩 빼준다
            days += int(maps[a][b]) #days에 수량을 더해준다
            for i in range(4):
                ddx = a + dx[i]
                ddy = b + dy[i]
                if ddx < 0 or ddx >= len(maps) or ddy < 0 or ddy >= len(maps[0]):   #범위 벗어나면 continue
                    continue
                else:
                    if maps[ddx][ddy] != 'X':
                        if visited[ddx][ddy] ==0:   #X가 아니고 방문하지 않은 곳이라면 q에 추가해주고 visited에 추가해준다
                            q.append([ddx,ddy])
                            visited[ddx][ddy] = 1
        return days #while문 종료되면 days return
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(dfs(i,j,visited))
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer