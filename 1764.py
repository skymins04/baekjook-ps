import sys
N,M=map(int,sys.stdin.readline().split())
dic={}
result=[]
length=0
for _ in range(N):
    s = sys.stdin.readline().strip()
    dic[hash(s)] = s
for _ in range(M):
    itm = dic.get(hash(sys.stdin.readline().strip()))
    if itm != None:
        result.append(itm)
        length += 1
result.sort()
print(length)
for i in result:
    print(i)