arr=input().split('-')
min = 0
for i in arr[0].split('+'):
    min += int(i.lstrip('0'))
arr.pop(0)
for i in arr:
    for j in i.split('+'):
        min -= int(j.lstrip('0'))
print(min)