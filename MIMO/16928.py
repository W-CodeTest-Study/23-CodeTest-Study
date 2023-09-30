import sys
from collections import deque
a,b = list(map(int, sys.stdin.readline().split()))
good = {}
bad = {}
answer = 0
board = 1
for i in range(a):
    n,m = list(map(int, sys.stdin.readline().split()))
    good[n] = m
for i in range(b):
    u,v= list(map(int, sys.stdin.readline().split()))
    bad[u] = v

q = deque()
board_cnt = [0] * 101
visited = [0] * 101
q = deque([1])
visited[1] = 1
while q:
    now = q.popleft()
    for i in range(1,7):
        check_move = now+i
        if 0 < check_move <= 100 and visited[check_move] == 0:
            if check_move in good:
                check_move = good[check_move]

            if check_move in bad:
                check_move = bad[check_move]

            if visited[check_move] == 0:
                q.append(check_move)
                visited[check_move] = 1
                board_cnt[check_move] = board_cnt[now] + 1
print(board_cnt[100])

