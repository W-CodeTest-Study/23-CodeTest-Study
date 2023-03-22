# 백준 3187 양치기 꿍
from collections import deque
# 1. 입력 - RXC개의 아래와 같은 문자가 주어진다.
# 빈공간 . 울타리 #, 늑대 v, 양 k
r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
visit = [[0]*c for _ in range(r) ]

# 2. 알고리즘
total = r*c # 전체 위치의 수
dydx = [[-1,0],[1,0],[0,1],[0,-1]] # 상하좌우
result_v = 0
result_k = 0
q = deque()

while sum(list(map(sum,visit))) != total:
    # 큐가 비었다면 방문하지 않은 곳 찾은 후 빠져나오기
    if not q:
        for i in range(r):
            for j in range(c):
                if visit[i][j] == "#":
                    visit[i][j] = 1
                if visit[i][j] == 0:
                    q.append([i,j])
                    break
            if q: break
    # 한 지역에 대해 dfs탐색을 한다.
    k, v = 0, 0
    while q:
        i, j = q.popleft()
        if visit[i][j] == 1: continue # 이미 방문한 곳이면 패스
        visit[i][j] = 1
        # 현재 늑대나 양인 경우 카운팅
        if maps[i][j] == "k":
            k += 1
        if maps[i][j] == "v":
            v += 1
        # 상하좌우 위치이고 #이 아닌 곳들을 큐에 넣음
        for dy, dx in dydx:
            if i+dy < 0 or j+dx < 0 or i+dy >= r or j+dx >= c:
                continue
            if maps[i+dy][j+dx] == "#":
                visit[i+dy][j+dx] = 1
                continue
            q.append([i+dy,j+dx])
    if v >= k: result_v += v
    if v < k: result_k += k
    # 해당 구역에서 양과 늑대 중 남는 동물에 대해 결과 값에 추가
print(result_k, result_v)