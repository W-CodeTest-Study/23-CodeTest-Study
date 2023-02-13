#문제 접근 : 문제를 보고 input, output을 보면서 1,0, 음수를 제외하고 나머지 수는 greedy로 해결하면 된다는 것을 발견하였다. 단순히 큰 수를 만드는 것이었기 때문에 이런 판단을 내렸다. 1은 뭐로 곱하든 1이 도움이 안되기 때문에 그냥 더해주는게 수를 크게 만든다 생각하였다. 0과 음수에 대해 여러가지 시행착오를 겪으면서 처리를 해주었는데, 우선은 음수 * 음수는 양수가 나오니까 음수 배열을 reverse = True로 정렬하고 맨 뒤부터 수를 곱해주었다. 그리고 남은 수들은 0이 있는지 체크하고 있다면 0 * 음수를 해주고, 없다면 음수를 그대로 더해 주었다. 


n = int(input())
cal = []
for i in range(n):
    a = int(input())
    cal.append(a) #배열추가
cal = sorted(cal) #greedy하기 위한 정렬
cnt = [] #1 이상의 수를 넣는 배열
ans = 0 #답 
countzero = 0 #zero가 몇개인지 count
underzero = [] #음수들이 들어가는 배열
while(len(cal)!= 0): 
    a = cal.pop()
    if a > 1:
        cnt.append(a) #1이상이면 cnt에 추가
    elif a == 0:
        countzero +=1 #0이면 countzero +=1
    elif a == 1:
        ans += 1 #1이면 그냥 덧셈
    elif a <0:
        underzero.append(a) #음수이면 underzero에 추가
    if len(cnt) == 2:
        ans += cnt[0] * cnt[1]
        cnt = []
if len(cnt) != 0:
    ans += cnt[0]
underzero = sorted(underzero, reverse=True)
while(len(underzero) > 1): #길이가 1 이상일 때 두개씩 빼줘서 곱한 뒤 ans에 추가
    b = underzero.pop()
    c = underzero.pop()
    ans += b*c
if len(underzero) ==1: #음수 1개 남았다면 0 있는지 체크하고 없으면 그냥 덧셈, 있으면 제거
    if countzero == 0:
        ans += underzero[0]
print(ans)