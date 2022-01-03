'''
    No: 2581
    Title: 소수
    Problem:
        자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
        예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
    Input:
        입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
        M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
    Output:
        M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
        단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
    Lang:
        Python 3
    Explanation:
        에라토스테네스의 체를 이용해 시간복잡도를 줄이는 작업이 필요함.
'''

M=int(input()) # 표준 입력 처리
N=int(input())
pns=[] # 주어진 범위 내의 소수를 포함하는 리스트
arr=[True]*(N+1) # 에라토스테네스의 체를 이용한 소수 탐색을 위해 사용하는 리스트, True로 이루어진 N+1 길이의 리스트
for i in range(2,N+1): # 2부터 N까지 반복
    if arr[i]: # arr[i]가 True(소수)일 경우에만 하위 작업 수행
        for j in range(2,N//i+1): # 소수의 배수를 모두 소수가 아닌 수로 마킹
            arr[i*j]=False
        if i>=M: # 탐색된 소수가 범위 내에 있는지 검사 후 리스트에 추가
            pns.append(i)
if len(pns) > 0: # 범위 내 소수가 존재할 경우
    print(sum(pns)) # 소수의 총합
    print(min(pns)) # 범위 내 소수들 중 최솟값
else: # 범위 내 소수가 존재하지 않을 경우
    print(-1)