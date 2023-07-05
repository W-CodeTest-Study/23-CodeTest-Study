# 프로그래머스 - 바탕화면 정리 (lv1)
def solution(wallpaper):
    top, left, bottom, right = -1,-1,-1,-1

    # # 가장 top에 있는 값
    for i in range(len(wallpaper)):
        if wallpaper[i].find("#") != -1:
            top = i
            break

    # # 가장 bottom에 있는 값
    for i in range(len(wallpaper)-1,-1,-1):
        if wallpaper[i].find("#") != -1:
            bottom = i + 1
            break

    # 가장 left에 있는 값
    for i in range(len(wallpaper[0])):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":
                left = i
                break
        if left != -1: break

    # 가장 right에 있는 값
    for i in range(len(wallpaper[0])-1,-1,-1):
        for j in range(len(wallpaper)):
            if wallpaper[j][i] == "#":
                right = i + 1
                break
        if right != -1: break

    return [top, left, bottom,right]