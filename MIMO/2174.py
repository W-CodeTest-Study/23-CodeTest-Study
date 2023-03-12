#문제 접근 : 딱히 어려운 알고리즘 없이 문제에서 요구하는 바를 순서대로 작성해 주면 되겠다는 생각을 하였다. 문제에서 요구하는 좌표계와 흔히 생각하는 좌표계가 달랐기 때문에 이부분만 주의하면 수월하게 풀 수 있으리란 생각을 했다.


import sys

a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
robot = []
dx = [0,-1,0,1]
dy = [-1,0,1,0] #방향성 설정을 위해 dx, dy를 설정해준다. 이 때 W N E S 순서대로 배치되게 해야 한다.
visited = [[0]*a for _ in range(b)] #특정 좌표에 어떤 로봇이 있는지 기록하기 위해 visited배열을 둔다
robotnum = 0
errorstr = []   #에러가 발생할 때의 경고문구를 기록하기 위한 배열
#     W N E S
for i in range(n):  #입력을 받아 주면서 위치를 숫자로 세팅한 후 좌표계를 보기 쉽게 0,0 ~ 으로 설정해준다
    robotnum += 1
    x, y, f = sys.stdin.readline().split()
    location = 0
    if f == "E":
        location = 2
    elif f == "N":
        location = 1
    elif f == "W":
        location = 0
    elif f == "S":
        location = 3
    x, y = int(x), int(y)
    visited[b-y][x-1] = robotnum    #새로운 좌표계로 visited배열에 로봇 존재 세팅
    robot.append([b-y, x-1, location])
for i in range(m):
    r, command, count = sys.stdin.readline().split()
    r,count = int(r), int(count)
    for j in range(count):
        if command == "L":  #L이면 왼쪽으로 돌려줘야 하기 때문에 -1
            robot[r-1][2] -= 1
            if robot[r-1][2] == -1:
                robot[r-1][2] = 3
        elif command == "R": #R이면 오른쪽으로 돌려줘야 하기 때문에 +1
            robot[r-1][2] += 1
            if robot[r-1][2] == 4:
                robot[r-1][2] = 0
        elif command == "F":    #F일 때
            ddx = robot[r-1][0] + dx[robot[r-1][2]]
            ddy = robot[r-1][1] + dy[robot[r-1][2]] #바뀌는 위치를 우선 저장
            if ddx < 0  or ddx > b-1 or ddy < 0 or ddy > a-1:   #범위를 벗어나면 에러문구 추가
                errorstr.append("Robot {} crashes into the wall".format(r))
            elif visited[ddx][ddy] != 0:    #다른 로봇이 있는 위치에 가면 에러문구 추가
                errorstr.append("Robot {} crashes into robot {}".format(r, visited[ddx][ddy]))
            else:   #위 에러가 안뜨면 visited세팅, robot 좌표도 변경
                visited[robot[r-1][0]][robot[r-1][1]] = 0
                visited[ddx][ddy] = r
                robot[r-1][0] = ddx
                robot[r-1][1] = ddy
if len(errorstr) == 0:
    print("OK")
else:
    print(errorstr[0])

