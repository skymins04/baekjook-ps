'''
    No: 1929
    Title: 소수 구하기
    Problem:
        M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
    Input:
        첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
    Output:
        한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
    Lang:
        Python 3
    Explanation:
        에라토스테네스의 체를 이용해 시간복잡도를 줄이는 작업이 필요함.    
'''

M,N=map(int,input().split()) # 표준입력 처리
arr=[True]*(N+1) # True로 이루어진 N+1개의 리스트 생성
for i in range(2,N+1): # 2부터 N까지 반복
    if arr[i]: # arr[i]가 True(소수)일 경우 하위 작업을 수행
        for j in range(2, N//i+1): # N이하의 i의 배수 개수를 x라 할때, i의 2배수 ~ i의 x배수를 index로 하는 요소에 False(소수가 아님)를 대입
            arr[i*j]=False
        if M<=i: # 소수인 arr[i]가 M보다 큰거나 같은지 검사, 참이면 i를 출력
            print(i)