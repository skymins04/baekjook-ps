from collections import Counter
import sys
N=int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

mode = Counter(arr).most_common()

print(round(sum(arr)/N))
print(arr[N//2])
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
print(arr[-1]-arr[0])