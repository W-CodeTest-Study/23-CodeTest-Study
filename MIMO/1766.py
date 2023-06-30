import heapq
n, m = map(int, input().split())
indegree = [0] * (n + 1) #진입차수는 0으로 초기화
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수를 1 증가

def topology_sort(): # 위상 정렬 함수
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = []
    for i in range(1, n + 1): # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q: # 큐가 빌 때까지 반복
        now = heapq.heappop(q) # 큐에서 원소 꺼내기
        result.append(now)
        for i in graph[now]: # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
            indegree[i] -= 1
            if indegree[i] == 0: # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                heapq.heappush(q,i)

    for i in result:
        print(i, end=' ')

topology_sort()