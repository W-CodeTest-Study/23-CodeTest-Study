#문제 접근 : 보자마자 딕셔너리로 풀어야 겠다는 생각을 했다. 문제를 풀면서 어려웠던 점은 입력을 받을 때 몇 개를 입력받는지 모르는데 입력을 받아야 하는 점이었다. 
import sys

tree = {}
cnt = 0
while True:
    n = sys.stdin.readline().rstrip()
    if not n:
        break
    n = str(n)
    if n not in tree:
        tree[n] = 1
    else:
        tree[n] += 1
    cnt +=1
caltree = []
for k,v in tree.items():
    caltree.append([k, round((v/cnt)*100,4)])
caltree = sorted(caltree, key = lambda x:x[0])
for a,b in caltree:
    print(a,"{:.4f}".format(b))