#문제 접근 : 알고리즘적 이해보다는 문제 해석이 더 어려웠던 문제다. 수학적으로 어떻게 해줘야 할지 잘 생각해줘야 한다. 문제를 해결해주기 위해 로프가 들어있는 배열을 돌아주면서 순서를 역순으로 곱하면서 얼마나 들 수 있는지를 비교해가며 문제를 해결해 주었다.
N = int(input())
rofe = []
maxrofe = -1
for i in range(N):
    a = int(input())
    rofe.append(a)
rofe = sorted(rofe)
for j in range(N,0,-1):
    if rofe[N-j] * j > maxrofe:
        maxrofe = rofe[N-j] * j
print(maxrofe)