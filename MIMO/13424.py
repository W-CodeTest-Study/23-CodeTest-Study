#문제 접근 : 노드 간의 최소 거리를 최신화하는 다익스트라, 플로이드 워셜 알고리즘을 알고는 있었지만, 구현하는 방법을 몰랐기 때문에 많은 어려움이 있었다. 다익스트라를 공부하면서 푼 문제다
import sys
import heapq
INF = int(1e9)  #최댓값 정의
def dij(start): 
    distance[start] = 0 #우선 시작한 곳의 거리를 0으로 설정해둔다
    queue = []
    heapq.heappush(queue, (0,start))    #우선순위 큐를 사용하여 현재거리인 0과 start지점인 start를 넣어준다
    while queue:
        currentdis, currentdest = heapq.heappop(queue)  #현재 거리와 현재 있는 곳을 빼준다
        if distance[currentdest] < currentdis:  #지금까지 온 cost가 현재 있는 distance보다 크다면 더이상 해줄 필요가 없다
            continue
        for i in room[currentdest]:     #현재 있는 노드에서 갈 수 있는 노드들을 탐색해준다  
            cost = currentdis + i[1]    #지금까지 온 distance에서 현재 노드에서 갈 수 있는 노드의 거리를 더해준다
            if cost < distance[i[0]]:   #계산해준 cost가 start지점에서 i[0]까지의 거리인 distance[i[0]]보다 작다면 
                distance[i[0]] = cost   #최신화 시켜준다.
                heapq.heappush(queue,(cost,i[0]))   #해당 노드에서 다시 거리를 계산해주어야 하기 때문에 heapq에 넣어준다

n = int(input())
for i in range(n):
    N,M = map(int,sys.stdin.readline().split())
    room = [[] for _ in range(N+1)]
    total = [0] * (N+1)
    for j in range(M):
        a,b,c = map(int,sys.stdin.readline().split())
        room[a].append([b,c])
        room[b].append([a,c])
    K = int(input())
    friend = list(map(int,sys.stdin.readline().split()))    #여기까지 입력
    for i in friend:
        distance = [INF] * (N+1)    #distance 초기화 후
        dij(i)  #다익스트라 함수 실행
        for j in range(1, N+1):
            total[j] += distance[j] #친구의 수만큼 total을 더해주어야 하므로 for문 한 번 돌때마다 total배열 최신화
    cnt = INF
    minindex = 0
    for i in range(1,len(total)):
        if total[i] < cnt:
            cnt = total[i]
            minindex = i
    print(minindex)
