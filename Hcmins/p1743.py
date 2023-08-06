N, M, K = map(int, input().split())               # N:행, M:열, K:쓰레기 갯수
maps = [[0 for i in range(M)]for j in range(N)]  # 음식물쓰레기 좌표
check = []                                        # 음식물쓰레귀 좌표
answers = [1]

for i in range(K):
    r, c = map(int, input().split())
    check.append([r-1, c-1])
    maps[r-1][c-1] = 1

# #1:상, 2:하, 3:좌, 4:우
# def recur(maps, x, y,before):
#     # 범위를 넘어가면 0
#     if (x < 0 or x > M-1):
#         return 0
#     if (y < 0 or y > N-1):
#         return 0

#     if (maps[x][y] == 0):
#         return 0
#     else:
#         return 1

#     if(before==0):
#         return recur(maps, x-1, y)+recur(maps, x+1, y)+recur(x, y-1)+recur(x, y+1)
#     elif(before==1):
#         return recur(maps, x-1, y)+recur(maps, x+1, y)+recur(x, y-1)+recur(x, y+1)
#     elif(before==2):
#         return recur(maps, x-1, y)+recur(maps, x+1, y)+recur(x, y-1)+recur(x, y+1)
#     elif(before==3):
#         return recur(maps, x-1, y)+recur(maps, x+1, y)+recur(x, y-1)+recur(x, y+1)
#     elif(before==4):
#         return recur(maps, x-1, y)+recur(maps, x+1, y)+recur(x, y-1)+recur(x, y+1)


# for i in range(K):
#     x = check[i][0]
#     y = check[i][1]
#     area = recur(maps, x, y)
#     answers.append(area)

print(maps)
print(max(answers))
