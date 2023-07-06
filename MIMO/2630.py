import sys

n = int(input())
white = 0
blue = 0
maps = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    maps.append(a)

def paper(x,y,p):
    global white, blue
    firstpaper = maps[x][y]
    for i in range(x,x+p):
        for j in range(y,y+p):
            if maps[i][j] != firstpaper:
                paper(x,y,p//2)
                paper(x,y+p//2,p//2)
                paper(x+p//2,y,p//2)
                paper(x+p//2,y+p//2,p//2)
                return
    if firstpaper == "1":
        blue += 1
    elif firstpaper == "0":
        white += 1    
paper(0,0,n)
print(white)
print(blue)