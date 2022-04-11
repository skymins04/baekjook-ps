import sys
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
S=sys.stdin.readline()
cnt=0
i=1
j=0
while i<M-1:
    if S[i-1:i+2]=='IOI':
        j+=1
        if j==N:
            j-=1
            cnt+=1
        i+=1
    else:
        j=0
    i+=1
print(cnt)