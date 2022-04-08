N=int(input())
i = N
flag = True
result = []
def fn(_n):
    return _n + sum(list(map(int, list(str(_n)))))

while True:
    if fn(i) == N:
        result.append(i)
    i -= 1
    if i < int(N * 0.5):
        break

if len(result) == 0:
    print(0)
else:
    print(min(result))