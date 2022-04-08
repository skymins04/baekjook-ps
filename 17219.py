import sys
N,M=map(int, sys.stdin.readline().split())
dic={}
for _ in range(N):
    domain, pswd = sys.stdin.readline().strip().split()
    dic[hash(domain)] = pswd
for _ in range(M):
    print(dic.get(hash(sys.stdin.readline().strip())))