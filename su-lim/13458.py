# input
N = int(input())
student_list = []
student_list = list(map(int, input().split()))

B, C = map(int, input().split())

# main
result = 0
for student in student_list:
  student = student-B
  result += 1
  if student <= 0:
    continue
  R = student%C
  if R == 0:
    result += student//C
  else:
    result += student//C+1

print(result)