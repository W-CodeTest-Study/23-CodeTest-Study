#문제 접근 : 며칠 째 우연찮게 그래프 이론 문제를 풀고 있다. 문제를 보자마자 그래프가 연결 되어있는지 확인을 해야 한다 생각했다. 그렇기 때문에 바로 유니온 파인드 함수를 적용 시켜서 그래프가 연결되어 있는지 확인했다. 그래프가 연결되었는지는 한 번 가지고는 부족했다. 뒤에서 부모가 바뀔수 있었기 때문이다. 그래서 한번 더 부모 검사를 하고 최소비용을 계산하는 식으로 문제를 풀어 주었다
import sys
sys.setrecursionlimit(10**6)

N, M, k = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))
friend = []
parent = [i for i in range(N)]
cost = []
answer = 0
for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    friend.append([a-1,b-1])
friend = sorted(friend)

def find(x):    #find 함수
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b): #Union 함수
    a = find(a)
    b = find(b)
    if money[a] < money[b]: #그냥 정렬하는 것이 아니라 최소비용 기준으로 정렬해주어야 한다
        parent[b] = a
    else:
        parent[a] = b
for i in friend:   
    u,v = i
    if find(u) !=find(v):
        union(u,v)
for i in range(N):  #한번 더 돌면서 parent와 root가 다른게 있는지 확인해준다
    if find(i) != parent[i]:
        parent[i] = find(i)
for i in parent:
    if i not in cost:
        cost.append(i)
for j in cost:
    answer += money[j]
if answer > k:
    print("Oh no")
else:
    print(answer)