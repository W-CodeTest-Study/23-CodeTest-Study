def solution(s, n):
    answer=''
    for i in s:
        if i.isalpha()==True:
            if 65<=ord(i)<=90:
                if ord(i)+n>90:
                    answer+=chr(ord(i)-26+n)
                else:
                    answer+=chr(ord(i)+n)
            else:
                if ord(i)+n>122:
                    answer+=chr(ord(i)-26+n)
                else:
                    answer+=chr(ord(i)+n)
        else:
            answer+=i
    return answer