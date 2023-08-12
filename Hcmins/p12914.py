# 방법1: 재귀 -> 너무 깊어져서 런타임에러뜸;;
# def recur(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     return recur(n-1)+recur(n-2)

# def solution(n):
#     answer = recur(n)
#     return answer%1234567

# 방법2 : 반복문 ->이것도 시간초과뜸
# def solution(n):
#     answer = 0
#     stack=[n]
#     while stack:
#         num = stack.pop()
#         if num==1:
#             answer+=1
#         elif num==2:
#             answer+=2
#         else:
#             stack.append(num-1)
#             stack.append(num-2)

#     return answer%1234567


# 방법3: DP 이전값을 배열에 저장해두어서 그 값이 또 필요할땐 저장된 값 사용 -> 정답!
def solution(n):
    answer = 0
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(1)
        elif i == 1:
            arr.append(2)
        else:
            arr.append(arr[i-1]+arr[i-2])
    return arr[n-1] % 1234567
