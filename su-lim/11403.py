# 백준 11403 경로찾기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n)]
matrix = [[0] * n for _ in range(n)]

for i in range(n):
	row = list(map(int,input().split()))
	for j in range(n):
		if row[j] == 1:
			graph[i].append(j)

q = deque()
for i in range(n):
	q.append((i, graph[i]))

while q:
	start, end = q.popleft()
	for e in end:
		if matrix[start][e] == 1:
			continue
		matrix[start][e] = 1
		q.append((start, graph[e]))

# print
for row in matrix:
	print(" ".join(map(str,row)))