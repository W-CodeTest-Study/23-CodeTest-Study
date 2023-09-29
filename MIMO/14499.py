##문제 복기 : 주사위가 굴러갈 때마다 어떻게 되는지 알아내는게 포인트, 머릿속에서 잘 굴리다보면 규칙이 나온다.

import sys
from collections import deque
wei = deque([4,1,3])
hei = deque([2,1,5,6])
dice = [0,0,0,0,0,0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
N,M,x,y,K = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    board.append(a)
order = list(map(int, sys.stdin.readline().split()))
up = 1
for j in order:
    if x+dx[j-1] < 0 or x+dx[j-1] >=N or y+dy[j-1]<0 or y+dy[j-1]>=M:
        continue
    else:
        x += dx[j-1]
        y += dy[j-1]
        if j == 1:
            cnt = wei.pop()
            cnt1 = hei.pop()
            hei.append(cnt)
            wei.appendleft(cnt1)
            hei[1] = wei[1]
        elif j == 2:
            cnt = wei.popleft()
            cnt1 = hei.pop()
            wei.append(cnt1)
            hei.append(cnt)
            hei[1] = wei[1]
        elif j == 3:
            hei.append(hei.popleft())
            wei[1] = hei[1]
        elif j == 4:
            hei.appendleft(hei.pop())
            wei[1] = hei[1]
        up = hei[1]
        print(dice[up-1])
        if board[x][y] == 0:
            board[x][y] = dice[7-up-1]
        else:
            dice[7-up-1] = board[x][y]
            board[x][y] = 0