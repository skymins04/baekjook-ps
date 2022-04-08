import sys
K=int(sys.stdin.readline())
stk=[]
for _ in range(K):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        stk.pop()
    else:
        stk.append(tmp)
print(sum(stk))