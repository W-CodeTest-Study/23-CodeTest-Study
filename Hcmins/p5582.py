# 방법1:짧은 거 슬라이싱해서 큰거랑 비교
# str1 = input()
# str2 = input()
# str1_list = list(map(str, str1))
# str2_list = list(map(str, str2))
# answers = [0]
# def check_substr(str1, str2):
#     # 확인은 긴거 길이 - 짧은거 길이 +1 만큼만 확인하면 된다.
#     for i in range(len(str2)-len(str1)+1):
#         count = 0
#         for j in range(len(str1)):
#             if str1[j] == str2[i+j]:
#                 count += 1
#             else:
#                 if max(answers) < count:
#                     answers.append(count)
#                 count = 0
# # 첫번째input 문자열이 작은경우
# if len(str1_list) <= len(str2_list):
#     for i in range(len(str1_list)):
#         check_substr(str1_list[len(str1_list)-1-i:], str2_list)
# # 두번째 input 문자열이 작은경우
# else:
#     for i in range(len(str2_list)):
#         check_substr(str2_list[len(str2_list)-1-i:], str1_list)
# print(max(answers))


# 방법2: 반복문 1개 더 줄이기
# str1 = input()
# str2 = input()
# str1_list = list(map(str, str1))
# str2_list = list(map(str, str2))
# answers = [0]
# # 앞에는 짤은거, 뒤에는 긴 문자열
# def check_substr(str1, str2):
#     # 확인은 긴거 길이 - 짧은거 길이 +1 만큼만 확인하면 된다.
#     len_1 = len(str1)
#     len_2 = len(str2)
#     for i in range(len_1-1, len_2):
#         count = 0
#         for j in range(len(str1)):
#             if str1[j] == str2[i+j-len_1+1]:
#                 count += 1
#             else:
#                 if max(answers) < count:
#                     answers.append(count)
#                 count = 0
# if len(str1_list) <= len(str2_list):      #첫번째가 짧은 문자열
#     for i in range(len(str1_list)-1):
#         str2_list.append(-1)
#         str2_list.insert(0, -1)
#     check_substr(str1_list, str2_list)
# else:                                     #두번째가 짧은 문자열
#     for i in range(len(str2_list)-1):
#         str1_list.append(-1)
#         str1_list.insert(0, -1)
#     check_substr(str2_list, str1_list)
# print(max(answers))


# # 방법3: 정협이형코드보다가 리스트로 안바꿔줘도 문자열에 index접근가능하다는거보고 코드향상시켜봤지만 여전히 시간실패
# str_1 = input()
# str_2 = input()
# answers = [0]
# # 앞에는 짤은거, 뒤에는 긴 문자열
# def check_substr(str1, str2):
#     # 확인은 긴거 길이 - 짧은거 길이 +1 만큼만 확인하면 된다.
#     len_1 = len(str1)
#     len_2 = len(str2)
#     for i in range(len_1-1, len_2):
#         count = 0
#         for j in range(len(str1)):
#             if str1[j] == str2[i+j-len_1+1]:
#                 count += 1
#             else:
#                 if max(answers) < count:
#                     answers.append(count)
#                 count = 0
# if len(str_1) <= len(str_2):
#     adding_str = ";"*(len(str_1)-1)
#     str_3 = adding_str+str_2+adding_str
#     check_substr(str_1, str_3)
# else:
#     adding_str = ";"*(len(str_2)-1)
#     str_3 = adding_str+str_1+adding_str
#     check_substr(str_2, str_3)
# print(max(answers))


# 방법4(풀이참조)
str1 = input()
str2 = input()

dp = [[0 for j in range(len(str2))]for i in range(len(str1))]
answer = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+1
        if dp[i][j] > answer:
            answer = dp[i][j]
print(max(dp))
