N = int(input())
arr1 = []
arr2 = []
stk = []
result = []

for _ in range(N):
    arr1.append(int(input()))

i = 0
j = 0
while i < len(arr1):
    if len(stk) != 0:
        if stk[len(stk)-1] != arr1[i] and j == N:
            break
        while stk[len(stk)-1] == arr1[i]:
            arr2.append(stk.pop())
            result.append('-')
            i += 1
            if len(stk) == 0:
                break
    if j != N:
        j += 1
        stk.append(j)
        result.append('+')

if arr1 != arr2:
    print('NO')
else:
    for i in result:
        print(i)