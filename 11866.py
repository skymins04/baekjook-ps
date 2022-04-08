N,K=map(int,input().split())
arr = [_ for _ in range(1,N+1)]
result = []
i = -1
while len(arr) != 0:
    for _ in range(K):
        if i == len(arr)-1:
            i = 0
        else:
            i += 1
    result.append(str(arr.pop(i)))
    i -= 1
print('<'+', '.join(result)+'>')