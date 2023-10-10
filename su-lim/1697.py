import sys
from collections import deque

input = sys.stdin.readline

Q = deque([])
L = 100001
arr = [0 for _ in range(L)]

def search(N, K, Q):
  Q.append(N)

  while(Q):
    x = Q.popleft()

    if x == K:
      return arr[x]

    for j in [x*2, x+1, x-1]:
      if 0 <= j < L and arr[j] == 0 and j != N:
        arr[j] = arr[x] + 1
        Q.append(j)

N, K = map(int, input().split())
print(search(N, K, Q))