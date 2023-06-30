# 백준 - 1197 최소 스패닝 트리
import sys
input = sys.stdin.readline

# 1. 입력된 값을 각 변수에 저장한다.
V, E = map(int, input().split()) # V 정점의 개수, E 간선의 개수
parents = [i for i in range(V+1)] # 정점별 부모 노드를 저장하는 배열

weight_list = [] # 간선 정보를 저장하는 리스트 생성
for i in range(E):
  weight_list.append(list(map(int, input().split()))) # A와 B가 가중치 C로 연결되어 있다

# 2. 알고리즘 구현
# 2-1. 간선 정보를 가중치에 대해 오름차순 정렬한다.
weight_list.sort(key=lambda x: x[2])

# find(): 부모 노드를 찾는 함수
#         자기 자신이 부모가 아닌 경우 부모를 타고 올라가서 루트 노드를 구함
def find(x):
  if x != parents[x]:
    parents[x] = find(parents[x])
  return parents[x]

# 2-2. 오름차순 정렬한 배열을 가지고 앞에서 부터 접근한다.
#      부모가 다를 경우 간선에 추가
mst = 0
result = 0

for A, B, weight in weight_list:
  p_A, p_B = find(A), find(B) # 부모 구하기
  if p_A != p_B:
    if p_A > p_B:
      parents[p_A] = p_B
    else:
      parents[p_B] = p_A
    result += weight
    mst += 1
  # 종료 조건: mst 간선의 수가 정점-1개면 멈춘다.
  if mst == V-1:
    break

# 3. 최종 완성된 스패닝 트리의 가중치 합산을 출력한다.
print(result)