def solution(answers):
    answer=[]
    grade=[0,0,0]
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(0,len(answers)):
        if answers[i]==s1[i%5]:
            grade[0] += 1
        if answers[i] == s2[i%8]:
            grade[1] += 1
        if answers[i] == s3[i%10]:
            grade[2] += 1
    maxvalue = grade[0]
    for i in range(0,len(grade)):
        if maxvalue <= grade[i]:
            maxvalue = grade[i]
    for i in range(0,len(grade)):
        if maxvalue == grade[i]:
            answer.append(i+1)    
    return answer