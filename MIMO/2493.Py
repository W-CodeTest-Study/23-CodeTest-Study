#문제 접근 : 이전에 봤던 문제랑 유사한 면이 있어서 바로 스택을 사용해야 겠다는 생각이 들었다. 또한, 모두 다른 n개의 수가 들어오기 때문에 position을 정할 때에도 딕셔너리를 사용해서 위치를 잡아주어야 겠다는 생각을 하였다
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
stack = []
pos = {}    #위치를 잡아주기 위한 딕셔너리
for i in range(len(a)):
    pos[a[i]] = i
answer =[0]*n
for i in range(n-1, -1, -1):    #맨 마지막 인덱스부터 돌면서 스택에 넣어준다
    if len(stack) == 0: #스택이 비어있다면 바로 채우기
        stack.append(a[i])
    else:
        if stack[-1] < a[i]:    #마지막 스택보다 들어오려는 값이 크다면 
            cnt = stack.pop()   #마지막 스택을 빼주고
            answer[pos[cnt]] = i+1  #들어오려는 값의 인덱스를 빼준 값에 넣어준다
            while(True):    
                if len(stack) == 0:
                    stack.append(a[i])
                    break
                else:
                    if stack[-1] < a[i]:
                        cnt = stack.pop()
                        answer[pos[cnt]] = i+1
                    else:
                        stack.append(a[i])
                        break
        elif stack[-1] >= a[i]:
            stack.append(a[i])
print(*answer)