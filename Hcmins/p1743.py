# 첫시도 시간초과 나옴 : 처음에는 check를 deepcopy해서 모든 요소마다의 temp_check를 만들어서 음식물 쓰레기 최대값을 구했다.
# temp_check를 사용할 필요없이 어차피 같은 묶음이면 빼버려도 상관없다. 오히려 중복안되서 더 빠르게 실행할수있다.
# 다풀고 나니까 코드가 짧아서 신기하다. 되게 오랜시간 고민했던 문제인데,,
from collections import deque
check = []
N, M, K = map(int, input().split())               # N:행, M:열, K:쓰레기 갯수
for i in range(K):
    r, c = map(int, input().split())
    check.append([r-1, c-1])
    # 음식물쓰레귀 좌표
answers = [0]
# 얖옆에 있는 음식물만큼 세서 그 값을 리턴해준다.
# 여기서 세어진 음식물은 check에서 지워지고 stack에 담겨진다.


def count(x, y):
    count = 0
    s = [x+1, y]
    n = [x-1, y]
    w = [x, y-1]
    e = [x, y+1]
    if s in check:
        stack.append(s)
        check.remove(s)
        count += 1
    if n in check:
        stack.append(n)
        check.remove(n)
        count += 1
    if w in check:
        stack.append(w)
        check.remove(w)
        count += 1
    if e in check:
        stack.append(e)
        check.remove(e)
        count += 1
    return count


stack = deque()
while check:
    stack.append(check.pop())
    cnt = 1
    # 스택이 빌때까지 반복
    while stack:
        [x, y] = stack.pop()
        cnt += count(x, y)
        answers.append(cnt)
    # stack.clear()   #스택 어차피 while문 돌면서 비게 되어서 안해도 된다..!

print(max(answers))
