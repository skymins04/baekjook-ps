for _ in range(int(input())):
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = [False]*N
    arr2[M] = True
    cnt = 1
    
    while len(arr1) != 0:
        if len(arr1) == 1:
            break
        elif arr2[0] and max(arr1[1:]) <= arr1[0]:
            break
        elif max(arr1[1:]) > arr1[0]:
            arr1.append(arr1.pop(0))
            arr2.append(arr2.pop(0))
        else:
            cnt += 1
            arr1.pop(0)
            arr2.pop(0)
    print(cnt)