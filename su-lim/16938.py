# 백준 16938 - 캠프준비

# 조건
# - 난이도의 합은 L 보다 크거나 같고, R보다 작거나 같아야함
# - 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 함.
from itertools import combinations

# 1. 입력
N, sum_min, sum_max, sub_min = map(int, input().split())
probs = list(map(int, input().split()))

# 문제 세트가 담긴 배열 만들기
prob_set = []
for i in range(2,N+1):
  prob_set.extend(list(combinations(probs, i)))

# 2. 알고리즘
result = 0
for prob in prob_set:
  sum_prob = sum(prob)
  # sum_min 보다 크거나 같은가?
  if not sum_prob >= sum_min:
    continue
  # sum_max 보다 작거나 같은가?
  if not sum_prob <= sum_max:
    continue
  # 가장 어려운 문제와 가장 쉬운 문제의 난이도는 sub_min 보다 크거나 같은가?
  if not max(prob) - min(prob) >= sub_min:
    continue
  result+=1

print(result)