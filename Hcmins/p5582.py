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


# # 첫번째input 문자열이 작은경우
# if len(str1_list) <= len(str2_list):
#     for i in range(len(str1_list)-1):
#         str2_list.append(-1)
#         str2_list.insert(0, -1)
#     check_substr(str1_list, str2_list)
# # 두번째 input 문자열이 작은경우
# else:
#     for i in range(len(str2_list)-1):
#         str1_list.append(-1)
#         str1_list.insert(0, -1)
#     check_substr(str2_list, str1_list)
# print(max(answers))


str_1 = input()
str_2 = input()
answers = [0]

# 앞에는 짤은거, 뒤에는 긴 문자열


def check_substr(str1, str2):
    # 확인은 긴거 길이 - 짧은거 길이 +1 만큼만 확인하면 된다.
    len_1 = len(str1)
    len_2 = len(str2)
    for i in range(len_1-1, len_2):
        count = 0
        for j in range(len(str1)):
            if str1[j] == str2[i+j-len_1+1]:
                count += 1
            else:
                if max(answers) < count:
                    answers.append(count)
                count = 0


# 첫번째input 문자열이 작은경우
if len(str_1) <= len(str_2):
    adding_str = ";"*(len(str_1)-1)
    str_3 = adding_str+str_2+adding_str
    check_substr(str_1, str_3)
# 두번째 input 문자열이 작은경우
else:
    adding_str = ";"*(len(str_2)-1)
    str_3 = adding_str+str_1+adding_str
    check_substr(str_2, str_3)
print(max(answers))
