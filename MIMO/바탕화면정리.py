def solution(wallpaper):
    filex = []
    filey = []
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                filex.append(i)
                filey.append(j)
    answer.append(min(filex))
    answer.append(min(filey))
    answer.append(max(filex) + 1)
    answer.append(max(filey) + 1)
    return answer