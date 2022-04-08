N,M=map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in trees:
        if i >= mid:
            tmp += i-mid
    
    if M <= tmp:
        start = mid+1
    else:
        end = mid-1

print(end)