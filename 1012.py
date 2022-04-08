import sys

arr = []

def bfs(x, y, w, h):
    q = [(x,y)]
    while q:
        pos = q.pop(0)
        arr[pos[1]][pos[0]] = False
        if pos[1] != 0 and arr[pos[1]-1][pos[0]]:
            q.append((pos[0],pos[1]-1))
        if pos[1] != h-1 and arr[pos[1]+1][pos[0]]:
            q.append((pos[0],pos[1]+1))
        if pos[0] != 0 and arr[pos[1]][pos[0]-1]:
            q.append((pos[0]-1,pos[1]))
        if pos[0] != w-1 and arr[pos[1]][pos[0]+1]:
            q.append((pos[0]+1,pos[1]))

for _ in range(int(sys.stdin.readline())):
    M,N,K = map(int, sys.stdin.readline().split())
    arr = [[False for i in range(M)] for j in range(N)]
    cnt = 0
    for i in range(K):
        X,Y = map(int, sys.stdin.readline().split())
        arr[Y][X] = True

    for i in range(N):
        for j in range(M):
            if(arr[i][j]) :
                cnt += 1
                bfs(j, i, M, N)

    print(cnt)
                