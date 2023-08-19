N = int(input())
arr = []
for i in range(N):
    str = input()
    arr.append(list(str))

print(arr)
answer1 = 0
answer2 = 0

# return : 일반인이 볼때 갯수


def normal() -> int:
    return 0

# return : 적록색약이 볼때 갯수


def blind() -> int:
    return 0
