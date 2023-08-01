import sys
N = int(input())
a = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(a)-1
answer = [[start, end]]
mid = abs(a[0] + a[-1])
while (start < end):
    pivot = a[start] + a[end]
    if abs(pivot) < mid:
        mid = abs(pivot)
        answer.pop()
        answer.append([start,end])
    if pivot <= 0:
        start += 1
    elif pivot > 0:
        end -= 1
    if pivot == 0:
        break
print(a[answer[0][0]], a[answer[0][1]])
