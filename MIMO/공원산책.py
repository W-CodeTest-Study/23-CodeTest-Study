def solution(park, routes):
    answer = []
    maps = []
    for i in range(len(park)):
        cnt = []
        for j in range(len(park[i])):
            cnt.append(park[i][j])
        maps.append(cnt)
    x = 0
    y = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                x = i
                y = j
    for i in range(len(routes)):
        gomap = int(routes[i][2])
        test = True
        if routes[i][0] == "E":
            if 0<= y+gomap < len(maps[0]):
                for j in range(y, y+gomap+1):
                    if maps[x][j] == "X": 
                        test = False
                        break
                if test == True:
                    y += gomap
        elif routes[i][0] == "W":
            if 0<= y-gomap < len(maps[0]):
                for j in range(y-gomap, y+1):
                    if maps[x][j] == "X":
                        test = False
                        break
                if test == True:
                    y -= gomap  
        elif routes[i][0] == "S":
            if 0<= x+gomap < len(maps):
                for j in range(x, x+gomap+1):
                    if maps[j][y] == "X":
                        test = False
                        break
                if test == True:
                    x += gomap  
        elif routes[i][0] == "N":
            if 0<= x-gomap < len(maps):
                for j in range(x-gomap, x+1):
                    if maps[j][y] == "X":
                        test = False
                        break
                if test == True:
                    x -= gomap
    answer.append(x)
    answer.append(y)
    return answer