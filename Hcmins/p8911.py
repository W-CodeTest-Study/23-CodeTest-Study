rows = 500
cols = 2  # [x,y]
N = [0, 1]
S = [0, -1]
E = [1, 0]
W = [-1, 0]

# function that return rectangle_area in textcase


def turtle_control_program(textcase: str) -> int:
    # init var,start_pos,start_dir put in arr
    arr = [[0 for j in range(cols)]for i in range(rows)]  # deep copy
    current_pos = [0, 0]
    current_direction = N
    count = 0
    arr[count] = current_pos
    count += 1
    # fill in the arr for textcase
    for v in range(0, len(textcase)):
        op = textcase[v]
        if op == 'F':
            current_pos = [current_pos[0]+current_direction[0],
                           current_pos[1]+current_direction[1]]
            arr[count] = current_pos
            count += 1
            continue
        elif op == 'B':
            current_pos = [current_pos[0]-current_direction[0],
                           current_pos[1]-current_direction[1]]
            arr[count] = current_pos
            count += 1
            continue
        elif op == 'L':
            temp = current_direction[0]
            current_direction[0] = current_direction[1]
            current_direction[1] = temp
            if current_direction[0] == 0:
                current_direction[1] *= -1
            continue
        elif op == 'R':
            temp = current_direction[0]
            current_direction[0] = current_direction[1]
            current_direction[1] = temp
            if current_direction[1] == 0:
                current_direction[0] *= -1
            continue

        else:  # wrong operation is pass
            continue

    # find out min_x,max_x,min_y,max_y
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    for row in range(count):
        x = arr[row][0]
        y = arr[row][1]
        if max_x is None or x > max_x:
            max_x = x
        if max_y is None or y > max_y:
            max_y = y
        if min_x is None or x < min_x:
            min_x = x
        if min_y is None or y < min_y:
            min_y = y

    rectangle_area = (int(max_x) - int(min_x))*(int(max_y) - int(min_y))
    return rectangle_area


# input num of textcases, textcases
text_num = int(input())
textcases = [input() for _ in range(text_num)]

# print result
for textcase in textcases:
    print(turtle_control_program(textcase))


# N -> R -> E  R : x,y바꾸기
# N -> L -> W    : x,y바꾸고 -1 곱하기

# S -> R -> W   : x,y바꾸기
# S -> L -> E   : x,y바꾸고 -1 곱하기

# E -> R -> S : x,y바꾸고 -1
# E -> L -> N : x,y바꾸기

# W -> R -> N : x,y바꾸고 -1
# W -> L -> S : x,y바꾸기
