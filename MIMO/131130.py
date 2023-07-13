
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(cards):
    global parent 
    parent = [0] * (len(cards))
    dct = {}
    for i in range(0, len(cards)):
        parent[i] = i
    for j in range(len(cards)):
        for i in range(len(cards)):
            union(i, cards[i]-1)
    for p in range(len(parent)):
        if parent[p] not in dct:
            dct[parent[p]] = 1
        else:
            dct[parent[p]] += 1
        
    dct = list(dct.items())
    dct = sorted(dct, key = lambda x:x[1],reverse=True)
    
    if (len(dct) >=2):
        return (dct[0][1] * dct[1][1])
    else:
        return 0