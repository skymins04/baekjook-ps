for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    avg = sum(arr)/n
    student = 0
    for j in arr:
        if avg < j:
            student += 1
    print("{:.3f}%".format(round(i/n*100,3)))