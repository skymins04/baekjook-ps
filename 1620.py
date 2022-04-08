import sys
N,M=map(int,sys.stdin.readline().split())
dic1 = {}
dic2 = {}
for i in range(1,N+1):
    S=sys.stdin.readline().strip()
    dic1[str(i)]=S
    dic2[S]=i
for i in range(M):
    S=sys.stdin.readline().strip()
    S0=ord(S[0])
    if S0>=65 and S0<=122:
        print(dic2[S])
    else:
        print(dic1[S])