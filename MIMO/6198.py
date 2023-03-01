#문제 접근 : 골드 5라는 것을 보고 어렵겠거니 하고 문제를 읽었는데 굉장히 간단해서 for문 두 개로 해결했지만 시간초과가 떠버렸다. for문 2개로 했을 때 시간초과가 나면 stack을 사용하자는 것을 알고 있었기 때문에 바로 stack으로 바꿔줘서 문제를 해결할 수 있었다
n = int(input())
building = []
answer = 0
for i in range(n):  #n만큼 돌면서 입력을 받는다
    h = int(input())
    if len(building) == 0:  #stack이 비어있으면 그대로 building에 쌓아 올린다
        building.append(h)
    else:
        if building[-1] > h:    #stack이 비어있지 않고, 바로 이전 인덱스가 추가하려는 인덱스보다 크다면 쌓아 올린다
            answer += len(building)
            building.append(h)
        else:   #그 전 인덱스가 쌓아올리려는 인덱스보다 작다면
            building.pop()  #pop을 해준 뒤
            while(True):    #다른 요소들도 쌓아올리려는 인덱스보다 작을 수 있기 때문에 stack을 돌아준다
                if len(building) == 0:  #스택이 비어있다면 추가
                    building.append(h)
                    break;
                else:
                    if building[-1] > h:    #추가하려는 거 보다 더 큰 인덱스가 바로 앞에 있다면 stack을 쌓아올린다
                        answer += len(building)
                        building.append(h)
                        break
                    else:
                        building.pop()
print(answer)