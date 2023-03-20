#문제 접근 : 최소 스패닝트리 문제이다. 간선 입력을 받은 다음 정렬해준 다음 최소 간ㅓ선 부터 사이클을 이뤘는지 확인 후  계산
import sys
def parent(x):
    if graph[x] == x:
        return x
    graph[x] = parent(graph[x])
    return graph[x]
def union(a,b):
    a = parent(a)
    b = parent(b)
    if a<b:
        graph[b] = a
    else:
        graph[a] = b
n, m = map(int,sys.stdin.readline().split())
graph = [0]*(n+1)
arr = []
answer = 0
for i in range(n+1):
    graph[i] = i
for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    arr.append([a,b,c])
arr = sorted(arr, key = lambda x:x[2])
for i in arr:
    a,b,c = i
    if parent(a) != parent(b):  #싸이클 안  이뤘으면 +
        union(a,b)
        answer+=c
print(answer)
