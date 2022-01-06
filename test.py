L,C = map(int, input().split())
A = []
B = []
for c in input().split():
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        A.append(c)
    else:
        B.append(c)
caseA = []
caseB = []
result = []

def dfsA(_i, _l):
    if len(_l) > 0:
        caseA.append(_l[:])
    for i in range(_i, len(A)):
        _l += [A[i]]
        dfsA(i+1, _l)
        _l.pop(len(_l)-1)

def dfsB(_i, _l):
    if len(_l) > 1:
        caseB.append(_l[:])
    for i in range(_i, len(B)):
        _l += [B[i]]
        dfsB(i+1, _l)
        _l.pop(len(_l)-1)

dfsA(0, [])
dfsB(0, [])

for a in caseA:
    for b in caseB:
        if len(b) == L-len(a):
            result.append(''.join(sorted(a+b)))
result = sorted(result)

for i in result:
    print(i)