'''
    No: 11653
    Title: 소인수분해
    Problem:
        정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
    Input:
        첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
    Output:
        N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
    Lang:
        Python 3
    Explanation:
        N에 2부터 시작하는 i로 나누어보고 나머지가 0이면 해당 i값을 소인수로 출력하고, 아니라면 i값을 1 증가시키면서 소인수분해를 수행하면 된다.
        하지만 주어지는 정수 N의 범위가 1 ≤ N ≤ 10,000,000로 주어지기 때문에 N의 소인수분해 과정에서 나눠지는 수가 소수일 경우 불필요한 오버헤드가 발생한다.
        그래서 소수판별함수를 넣어 불필요한 오버헤드를 감소해야한다.
'''

# 소수 판별 함수
def isPN(n):
    if n > 1: # 1이 아닌 경우
        for i in range(2, int(n**0.5)+1): # 나누어지는 수가 있는지 검사
            if n%i == 0:
                return False
        return True
    else: # 1은 소수가 아님
        return False

N = int(input()) # 표준 입력 처리
if N != 1: # N이 1인 경우 아무것도 출력하지 않는다
    while True: # 소인수분해가 완료될 때까지 반복
        if isPN(N): # N이 소수라면 N을 출력하고 while문 종료
            print(N)
            break
        for i in range(2,N+1): # N이 소수가 아닐 경우, 소인수값 계산
            if N%i == 0: # 소인수값을 찾으면 N에 소인수로 나눈 값을 대입하고 해당 소인수를 출력후 for문 종료
                N = int(N/i)
                print(i)
                break