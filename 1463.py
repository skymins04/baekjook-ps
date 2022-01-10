'''
    No: 1463
    Title: 1로 만들기
    Problem:
        정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
            - X가 3으로 나누어 떨어지면, 3으로 나눈다.
            - X가 2로 나누어 떨어지면, 2로 나눈다.
            - 1을 뺀다.
        정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
    Input:
        첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
    Output:
        첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
    Lang:
        Python 3
    Explanation:
        Memoization을 통하 Bottom-Up DP를 통해 시간복잡도를 줄인다
'''

X=int(input()) # 표준 입력 처리
arr=[-1]*(X+3) # Memoization을 위한 리스트 선언 (IndexError를 피하기 위해 X+3 길이로 선언)
arr[1]=0 # Bottom-Up DP를 위해 기본값 대입
arr[2]=arr[3]=1
if arr[X] == -1: # 연산 전 리스트에 이미 결과값이 존재한다면 연산을 수행하지 않는다.
    i=4 # index가 4이상이어야 리스트에 결과값이 존재하지 않기 때문에 i를 4부터 시작해도 된다.
    while i<X+1: # i를 4부터 X까지 1씩 증가시키며 하위 연산 수행
        tmp=[arr[i-1]] # 1을 빼는 경우
        if i%2==0:
            tmp.append(arr[int(i/2)]) # 2를 나누는 경우
        if i%3==0:
            tmp.append(arr[int(i/3)]) # 3을 나누는 경우
        arr[i]=min(tmp)+1 # 위 3가지 경우 중 최소값에 1을 더하여 arr[i]에 대입
        i+=1 # index 1 증가
print(arr[X]) # 결과값 출력