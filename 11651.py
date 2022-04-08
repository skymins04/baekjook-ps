import sys
N=int(sys.stdin.readline())
arr=[]
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    arr.append([y, x])
arr.sort()
for i in arr:
    print("{} {}".format(i[1], i[0]))