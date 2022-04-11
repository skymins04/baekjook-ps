import sys
arr=[0]*12
arr[1]=1
arr[2]=2
arr[3]=4
idx=3
for _ in range(int(sys.stdin.readline())):
    N=int(sys.stdin.readline())
    if idx >= N:
        print(arr[N])
    else:
        for i in range(idx+1, N+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        print(arr[N])
        idx = N