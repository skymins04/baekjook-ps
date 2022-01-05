T=int(input())
for t in range(T):
    N,M=map(int, input().split())
    numerator = M
    denominator = N
    if N==M:
        print(1)
    else:
        for i in range(1, N):
            numerator *= M-i
            denominator *= N-i
        print(int(numerator/denominator))