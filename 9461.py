'''
    No: 9461
    Title: 파도반 수열
    Problem:
        오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 
        나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.
        파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.
        N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.
    Input:
        첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)
    Output:
        각 테스트 케이스마다 P(N)을 출력한다.
    Lang:
        Python 3
    Explanation:
        Bottom-Up Dynamic Programing을 통해 CallStack Overflow를 방지하고 시간복잡도를 줄여야한다.
        Memoization을 통해 O(1)의 공간복잡도로 해결할 수 있다.
        P(N) = P(N-2) + P(N-3) 이라는 규칙을 가지고있다.
'''

P = [-1,1,1,1,2,2,3,4,5,7,9] # DP Memoization을 위한 리스트 생성
P.extend([-1]*90) # N의 최대값은 100이기 때문에 index 100까지 -1으로 채움
mem = 10 # Memoization된 계산 결과의 범위 저장
T = int(input()) # 표준 입력 처리 - 테스트 케이스 개수
for t in range(T): # 테스트 케이스 반복
    N = int(input()) # 표준 입력 처리 - N
    if N > mem: # N이 Memoization된 범위 내가 아닐 경우에만 하위 작업 수행
        for i in range(mem+1, N+1): # 파도반 수열 계산
            P[i] = P[i-2] + P[i-3]
            mem += 1 # Memoization된 범위 업데이트
    print(P[N]) # 결과 출력