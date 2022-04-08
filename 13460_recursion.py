N,M=map(int,input().split())
board = []
rx = 0
ry = 0
bx = 0
xy = 0
counts = []
for i in range(N):
    board.append(list(input()))
    tmp = ''.join(board[i]).find('R')
    if tmp != -1:
        rx = tmp
        ry = i
    tmp = ''.join(board[i]).find('B')
    if tmp != -1:
        bx = tmp
        by = i
    
def copy(_arr):
    return [itm[:] for itm in _arr]

def checkWall(_board, _rx, _ry, _bx, _by):
    if _rx == _bx and _ry != _by:
        a = 0
        b = 0
        if _ry < _by:
            a = _ry
            b = _by
        else:
            a = _by
            b = _ry
        for i in range(a+1, b):
            if _board[i][_rx] == '#' or _board[i][_rx] == 'O':
                return True
    elif _ry == _by and _rx != _bx:
        a = 0
        b = 0
        if _rx < _bx:
            a = _rx
            b = _bx
        else:
            a = _bx
            b = _rx
        for i in range(a+1, b):
            if _board[_ry][i] == '#' or _board[_ry][i] == 'O':
                return True
    return False

def moveHorizontal(_b, _rx, _ry, _bx, _by, _gain, _cnt): # _gain = -1 : move left, _gain = 1 : move right
    if _cnt > 10:
        return
    if len(counts) != 0:
        if min(counts) < _cnt:
            return
    _board = copy(_b)
    _queue = []
    if _rx*(_gain*-1) <= _bx*(_gain*-1):
        _queue = [[_rx, _ry, 'R'], [_bx, _by, 'B']]
    else:
        _queue = [[_bx, _by, 'B'], [_rx, _ry, 'R']]
    for q in _queue:
        x = q[0]
        while x > 0 and x < M-1:
            x += _gain
            if _board[q[1]][x] == 'O':
                if q[2] == 'R' and _ry != _by:
                    counts.append(_cnt)
                elif q[2] == 'R' and _ry == _by and checkWall(_board, _rx, _ry, _bx, _by):
                    counts.append(_cnt)
                return
            elif _board[q[1]][x] != '.':
                x += _gain*-1
                break
        _board[q[1]][q[0]] = '.'
        _board[q[1]][x] = q[2]
        if q[2] == 'R':
            _rx = x
        else:
            _bx = x
    if _b == _board:
        return
    moveHorizontal(_board, _rx, _ry, _bx, _by, -1, _cnt+1)
    moveHorizontal(_board, _rx, _ry, _bx, _by, 1, _cnt+1)
    moveVertical(_board, _rx, _ry, _bx, _by, -1, _cnt+1)
    moveVertical(_board, _rx, _ry, _bx, _by, 1, _cnt+1)

def moveVertical(_b, _rx, _ry, _bx, _by, _gain, _cnt): # _gain = -1 : move up, _gain = 1 : move down
    if _cnt > 10:
        return
    if len(counts) != 0:
        if min(counts) < _cnt:
            return
    _board = copy(_b)
    _queue = []
    if _ry*(_gain*-1) <= _by*(_gain*-1):
        _queue = [[_rx, _ry, 'R'], [_bx, _by, 'B']]
    else:
        _queue = [[_bx, _by, 'B'], [_rx, _ry, 'R']]
    for q in _queue:
        y = q[1]
        while y > 0 and y < N-1:
            y += _gain
            if _board[y][q[0]] == 'O':
                if q[2] == 'R' and _rx != _bx:
                    counts.append(_cnt)
                elif q[2] == 'R' and _rx == _bx and checkWall(_board, _rx, _ry, _bx, _by):
                    counts.append(_cnt)
                return
            elif _board[y][q[0]] != '.':
                y += _gain*-1
                break
        _board[q[1]][q[0]] = '.'
        _board[y][q[0]] = q[2]
        if q[2] == 'R':
            _ry = y
        else:
            _by = y
    if _b == _board:
        return
    moveHorizontal(_board, _rx, _ry, _bx, _by, -1, _cnt+1)
    moveHorizontal(_board, _rx, _ry, _bx, _by, 1, _cnt+1)
    moveVertical(_board, _rx, _ry, _bx, _by, -1, _cnt+1)
    moveVertical(_board, _rx, _ry, _bx, _by, 1, _cnt+1)

moveHorizontal(board, rx, ry, bx, by, -1, 1)
moveHorizontal(board, rx, ry, bx, by, 1, 1)
moveVertical(board, rx, ry, bx, by, -1, 1)
moveVertical(board, rx, ry, bx, by, 1, 1)

if len(counts) == 0:
    print(-1)
else:
    print(min(counts))