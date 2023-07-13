a = int(input())
x = 0
y = 0
dx = [[0,1],[-1,0],[0,-1],[1,0]]
cnt = 0
for i in range(a):
    s = input()
    x,y = 0,0
    turtlemapx = []
    turtlemapy = []
    turtlemapx.append(0)
    turtlemapy.append(0)
    for j in s:
        if j == "F":
            x += dx[cnt][0]
            y += dx[cnt][1]
        elif j == "B":
            x -= dx[cnt][0]
            y -= dx[cnt][1]
        elif j == "L":
            cnt += 1
            cnt = cnt %4
        elif j == "R":
            cnt -= 1
            cnt = cnt %4 
        turtlemapx.append(x)
        turtlemapy.append(y)
    minx = min(turtlemapx)
    maxx = max(turtlemapx)
    miny = min(turtlemapy)
    maxy = max(turtlemapy)
    print((maxx-minx) * (maxy - miny))