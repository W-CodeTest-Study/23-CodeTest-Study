str1 = input()
str2 = input()
str1_list = list(map(str, str1))
str2_list = list(map(str, str2))

answers = [0]


def check_substr(str1, str2):
    # 확인은 긴거 길이 - 짧은거 길이 +1 만큼만 확인하면 된다.
    for i in range(len(str2)-len(str1)+1):
        count = 0
        for j in range(len(str1)):
            if str1[j] == str2[i+j]:
                count += 1
            else:
                if max(answers) < count:
                    answers.append(count)
                count = 0


# 첫번째input 문자열이 작은경우
if len(str1_list) <= len(str2_list):
    for i in range(len(str1_list)):
        check_substr(str1_list[len(str1_list)-1-i:], str2_list)

# 두번째 input 문자열이 작은경우
else:
    for i in range(len(str2_list)):
        check_substr(str2_list[len(str2_list)-1-i:], str1_list)


print(max(answers))
