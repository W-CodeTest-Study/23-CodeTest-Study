# input
T = int(input())

for test in range(T):
  N, K = map(int,input().split())

  string = list(input())
  unit = N//4
  string_list = []

  # 에러 코드
  # for _ in range(unit):# 회전

  #   for i in range(unit):
  #     string_list.append(string[i*unit:(i+1)*unit])

  #   string = string[-1] + string[0:N-1]

  for _ in range(unit):# 회전
    char = string.pop()
    string.insert(0,char)

    for i in range(4):
      tmp = ""
      for j in range(unit):
        tmp += string[unit*i+j]
      string_list.append(tmp)

  # 중복제거
  string_list = set(string_list)

  # 16진수 변환
  result_arr=[]
  for string in string_list:
    result_arr.append(int(string, 16))
  result_arr.sort(reverse=True)

  print("#"+str(test+1),result_arr[K-1])