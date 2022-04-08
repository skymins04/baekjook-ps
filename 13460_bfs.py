N,M=map(int, input().split()) #보드 사이즈 입력

board = [] #보드
for i in range(N): #보드 입력 받으며 빨간구슬과 파란구슬의 초기좌표 저장
    tmp = input()
    board.append(list(tmp))
    if tmp.find('R') != -1:
        rx = tmp.find('R')
        ry = i
    if tmp.find('B') != -1:
        bx = tmp.find('B')
        by = i

visited = [[[[False] * N for _ in range(M)] for _ in range(N)] for _ in range(M)] #방문처리를 위한 hash-set
visited[rx][ry][bx][by] = True #초기위치 방문처리
queue = [(rx, ry, bx, by, 1)] #작업 큐

dx = [-1,1,0,0] #변화값 (좌,우,상,하)
dy = [0,0,-1,1]

def move(_x, _y, _dx, _dy): #구슬 움직이기
    cnt = 0
    while board[_y+_dy][_x+_dx] != '#' and board[_y][_x] != 'O': #이동한 좌표가 벽이 아니고 현위치가 구멍이 아닐 때까지 좌표에 변화량을 더함
        _x += _dx
        _y += _dy
        cnt += 1
    return _x, _y, cnt #이동된 좌표와 이동량을 리턴

def bfs():
    while queue: #작업 큐가 비어있다면 종료
        rx, ry, bx, by, depth = queue.pop(0) #작업큐에서 좌표값 가져오기
        if depth > 10: # depth 검사
            break
        for i in range(4): # 현재 좌표에서 좌우상하 각 방향으로 이동하는 루프
            rx_tmp, ry_tmp, rcnt_tmp = move(rx, ry, dx[i], dy[i]) #빨간구슬 움직이기
            bx_tmp, by_tmp, bcnt_tmp = move(bx, by, dx[i], dy[i]) #파란구슬 움직이기

            if board[by_tmp][bx_tmp] == 'O': #파란구슬이 구멍에 들어갈 경우 건너뛰기
                continue
            elif board[ry_tmp][rx_tmp] == 'O': #빨간구슬이 구멍에 들어갈 경우 횟수 출력 후 종료 (depth가 커지는 방향으로 탐색하기 때문에 바로 종료해도 됨)
                print(depth)
                return

            if rx_tmp == bx_tmp and ry_tmp == by_tmp: #빨간구슬과 파란구슬이 겹친 경우, 이동량을 비교하여 정렬
                if rcnt_tmp > bcnt_tmp: #빨간구슬이 더 많이 움직인 경우
                    rx_tmp -= dx[i]
                    ry_tmp -= dy[i]
                else: #파란구슬이 더 많이 움직인 경우
                    bx_tmp -= dx[i]
                    by_tmp -= dy[i]
            
            if visited[rx_tmp][ry_tmp][bx_tmp][by_tmp] == False: #방문하지 않은 좌표조합을 방문처리하고 작업큐에 추가
                visited[rx_tmp][ry_tmp][bx_tmp][by_tmp] = True
                queue.append((rx_tmp, ry_tmp, bx_tmp, by_tmp, depth+1))
    print(-1) #depth 10 이내로 완료할 수 없다면 -1 출력 후 종료

bfs()