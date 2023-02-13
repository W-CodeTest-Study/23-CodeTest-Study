import sys

a = int(input())
for i in range(a):
    m,n = map(int, sys.stdin.readline().split())
    print(m-1)
    for j in range(n):
        b,c = map(int, sys.stdin.readline().split())