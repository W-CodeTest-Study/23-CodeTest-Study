N = int(input())
map = []
answer1, answer2 = 0, 0
for i in range(N):
    str = input()
    map.append(list(str))
# 상하좌우보면서 같은색은 stack에서 제거해준다.


def count(x, y, color):
    s = [x, y+1]
    n = [x, y-1]
    e = [x+1, y]
    w = [x-1, y]
    if s in stack and map[s[0]][s[1]] == color:
        stack.remove(s)
        count(s[0], s[1], color)
    if n in stack and map[n[0]][n[1]] == color:
        stack.remove(n)
        count(n[0], n[1], color)
    if e in stack and map[e[0]][e[1]] == color:
        stack.remove(e)
        count(e[0], e[1], color)
    if w in stack and map[w[0]][w[1]] == color:
        stack.remove(w)
        count(w[0], w[1], color)
    return 1


# 정상일 경우
stack = []
for i in range(N):
    for j in range(N):
        stack.append([i, j])
color = map[0][0]
while stack:
    point = stack.pop()
    x, y = point[0], point[1]
    color = map[x][y]
    answer1 += count(x, y, color)
# 비정상일경우
for i in range(N):
    for j in range(N):
        stack.append([i, j])
        if map[i][j] == 'G':
            map[i][j] = 'R'
color = map[0][0]
while stack:
    point = stack.pop()
    x, y = point[0], point[1]
    color = map[x][y]
    answer2 += count(x, y, color)

print(answer1, answer2)
