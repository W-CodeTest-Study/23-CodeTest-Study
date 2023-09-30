# https://www.acmicpc.net/problem/2467

# 테스트용
from sys import stdin as s
s = open("input.txt","rt")
n = int(s.readline().strip())
arr = list(s.readline().strip().split(" "))
# 절대 경로도 되고, 상대 경로도 된다.
# r read t text

# 제출용
# n = int(input().strip())
# arr = list(input().strip().split(" "))

result = 2000000000
answerX = 0
answerY = 0
x = 0
y = n-1

while x < y:
    sum = int(arr[x]) + int(arr[y])

    if abs(sum) < result:
        result = abs(sum)
        answerX = x
        answerY = y

    if sum < 0 :
        x += 1
    else:
        y -= 1

print(arr[answerX], arr[answerY])
