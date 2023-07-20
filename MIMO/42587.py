def solution(priorities, location):
    stack=[]
    answer={}
    i=0
    while(sum(priorities)!=0):
        a=max(priorities)
        if i>=len(priorities):
            i=0
        if priorities[i]==a:
            answer[i]=priorities[i]
            priorities[i]=0
            i+=1
        else:
            i+=1
    ans=list(answer.keys())
    return ans.index(location)+1