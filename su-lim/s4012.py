def my_sum(arr):
  result = 0
  for i in range(len(arr)):
    for j in range(len(arr)):
      result += maps[arr[i]][arr[j]]
  return result

# 조합 구하기
def search(idx, cnt):

  global MIN

  if cnt == N//2:
    # S1과 S2 요소 구하고 -> 시너지 구하고 -> MIN 업데이트
    S1, S2 = [], []
    for i in range(N):
      if check[i] == 1:
        S1.append(i)
      if check[i] == 0:
        S2.append(i)
    MIN = min(MIN, abs(my_sum(S1)-my_sum(S2)))
    return
  else:
    for i in range(idx, N):
      if check[i] == 0:
        check[i] = 1
        search(i, cnt+1)
        check[i] = 0

# 입력 구현
T = int(input())
for test_number in range(1,T+1):

  N = int(input())
  maps = [list(map(int, input().split())) for _ in range(N)]
  check = [0] * N

  MIN = float("inf")
  search(0, 0)
  print("#"+str(test_number), MIN)