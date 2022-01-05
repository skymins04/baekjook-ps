arr=list(map(int,input().split()))
checksum = 0
for x in arr:
    checksum += x**2
print(checksum%10)