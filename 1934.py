'''
    No: 1934
    Title: 최소공배수
    Problem:
        두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
        이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 
        예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
        두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
    Input:
        첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)
    Output:
        첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.
    Lang:
        Python 3
    Explanation:
        주어진 A, B에 대하여, 유클리드 호제법을 통해 A와 B의 GCD를 구하고, (A*B/GCD)를 통해 LCM을 구하면 된다.
'''

T = int(input()) # 표준 입력 처리 - 테스트케이스 개수
for t in  range(T): # 테스트케이스 반복
    tmp = list(map(int, input().split())) # 표준 입력 처리 - A, B
    big = max(tmp) # A와 B 중 더 큰 수
    small = min(tmp) # A와 B 중 더 작은 수
    gcd = big % small # gcd가 저장될 변수 
    tmp = big * small # A*B를 저장해둔 변수
    while gcd != 0:
        big = small
        small = gcd
        gcd = big % small
    gcd = small
    print(int(tmp/gcd))