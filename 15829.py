# def getCode(c):
#     return ord(c)-96
# result = 0
# L=int(input())
# for idx, val in enumerate(list(map(getCode, list(input())))):
#     result += val * (31**idx)
# print(result)

L=int(input())
s=input()
result=0
for i in range(L):
    result += (ord(s[i])-96)*(31**i)
print(result%1234567891)