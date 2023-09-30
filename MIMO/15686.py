import sys
from itertools import combinations

N,M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    board.append(a)
chicken = []
house = []
answer = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i,j])
        elif board[i][j] == 1:
            house.append([i,j])
allcount = list(combinations(chicken,M))
for i in range(len(allcount)):
    chickendistance = 0
    housedistance = [9999 for _ in range(len(house))]
    for j in range(len(allcount[i])):
        x = allcount[i][j][0]
        y = allcount[i][j][1]
        for k in range(len(house)):
            tmp = abs(house[k][0] - x) + abs(house[k][1] - y)
            if housedistance[k] > tmp:
                housedistance[k] = tmp
    answer.append(sum(housedistance))
print(min(answer))