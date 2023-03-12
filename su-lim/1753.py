# 백준 / 1753 최단경로

import sys, heapq
input = sys.stdin.readline
MAX = sys.maxsize

# input
V, E = map(int,input().split())
start = int(input())

# init
distance = [MAX] * (V+1)
graph = [ [] for _ in range(V+1)]

for _ in range(E):
	u,v,w = map(int, input().split())
	graph[u].append((v,w))

def dijkstra(start):
	heap = [] 
	# 초기 값으로 start와 연결된 그래프들 확인 (연결안되어 있으면 차피 INF), start->start는 거리 0이므로 0, start
	heapq.heappush(heap, (0, start)) 
	distance[start] = 0;

	while heap: # q가 빌 때 까지 반복
		dist, now = heapq.heappop(heap)

		if distance[now] < dist: # 이미 방문한 적있는 경우
			continue

		for v, w in graph[now]:
			# start->v 보다 start->now->v 로 가는 방법이 더 작으면 업데이트
			cost = dist + w # start->now->v
			if cost < distance[v]:
				distance[v] = cost
				heapq.heappush(heap, (cost,v))

		# print("\n\ndistance\n", distance)
		# print("\n\nheap\n", heap)

dijkstra(start)
# print
for i in range(1, V+1):
	print(distance[i] if distance[i] != MAX else "INF")