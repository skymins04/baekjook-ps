from sys import stdin
n = int(input())
arr = []
for _ in range(n): 
    arr.append(list(map(int, stdin.readline().split())))
arr.sort()
for i in arr:
    print('{} {}'.format(i[0], i[1]))