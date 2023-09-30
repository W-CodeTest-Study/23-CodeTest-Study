
# 첫번째 시도방법 ( 메모리 초과 )
# N = int(input())
# arr = list(map(int, input().split()))
# answers = {}  # key에는 두 요소 합친 절대값, value는 두 요소의 index 쌍
# # arr.sort() :입력이 오른차순으로 들어옴
# for i in range(0, N):
#     for j in range(i+1, N):
#         answers[abs(arr[i]+arr[j])] = [i, j]
# key = min(answers.keys())
# first_index = answers[key][0]
# second_index = answers[key][1]
# print(arr[first_index], arr[second_index])


# 두번째 시도방법(시간초과)
# N = int(input())
# arr = list(map(int, input().split()))
# min = abs(arr[0]+arr[1])
# answer1 = 0
# answer2 = 0
# for i in range(0, N):
#     for j in range(i+1, N):
#         if (abs(arr[i]+arr[j]) < min):
#             min = abs(arr[i]+arr[j])
#             answer1 = arr[i]
#             answer2 = arr[j]
# print(answer1, answer2)

# 세번째 (풀이참조:투포인터)
N = int(input())
arr = list(map(int, input().split()))
mininum = 1000000000
index_1, index_2 = 0, N-1
x, y = 0, 0
while index_1 < index_2:
    cur = arr[index_1]+arr[index_2]
    if (abs(cur) <= mininum):
        x = arr[index_1]
        y = arr[index_2]
        mininum = abs(cur)
    if cur < 0:
        index_1 += 1
    elif cur == 0:
        break
    else:
        index_2 -= 1

print(x, y)
