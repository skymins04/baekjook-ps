'''
    No: 2609
    Title: 최대공약수와 최소공배수
    Problem:
        두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
    Input:
        첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
    Output:
        첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
    Lang:
        Python 3
    Explanation:
        최대공약수는 "유클리드 호제법"을 사용하고, 최소공배수는 (두 수의 곱) / (두 수의 최대공약수)로 구할 수 있다.
'''

a, b = map(int, input().split()) # 표준 입출력 처리

#최대공약수 산출 파트
big = a # 큰값과 작은값을 구분
small = b
if a < b:
    big = b
    small = a
mod = big % small # 첫번째 Moduler 연산 수행
while True:
    if mod == 0: # Moduler 연산값이 0이면, small 값이 최대공약수이다
        print(small)
        break
    big = small # Moduler 연산값이 0이 아니면, 값을 스왑하고 다시 Moduler 연산 수행
    small = mod
    mod = big % small

#최소공배구 산출 파트
print(int(a*b/small)) # 정수만 얻으면 되니 int로 형변환