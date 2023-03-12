#문제 접근 : 단순 bfs문제이다. BFS를 돌면서 거리도 계산해 주어야 한다. 처음에는 그래프를 딕셔너리에 넣고 계산을 해주어서 양방향 그래프를 구현해내지 못했는데 바로 이차원 그래프를 사용해서 양방향 그래프로 만들어 계산을 해주었다
import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
farm = [[]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
distance = {}
dis = 0
q = deque()
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    farm[a].append(b)
    farm[b].append(a)
q.append(farm[1])   #1부터 시작해야 하니까 무조건 1에 있는 값들을 빼준다.
visited[1] = 1  #1을 빼줬으니 visited[1] = 1로 설정
while(q):   #q가 빌때까지 반복문
    dis+=1
    cntar = []  #q에 거리만큼 한번에 넣어주어야 하기 때문에 배열을 따로 선언한다
    cnt = q.popleft()   #q에서 popleft한 값들을 cnt에 저장
    for i in cnt:
        visited[i] = 1
    for i in cnt:   #cnt를 돌면서 거리를 저장하는 distance 딕셔너리에 추가를 해준다
        if dis not in distance:
            distance[dis] = [i]
        else:
            distance[dis].append(i)
        for j in farm[i]:   #distance추가를 다 한 뒤 더 갈 수 있는 곳인지를 확인한다
            if visited[j] == 0:
                cntar.append(j)
    if len(cntar) !=0:
        q.append(list(set(cntar)))
answer = sorted(distance[dis])
print(answer[0], dis, len(distance[dis]))
