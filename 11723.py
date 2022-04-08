import sys
arr = [False]*21
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'add':
        arr[int(cmd[1])] = True
    elif cmd[0] == 'remove':
        arr[int(cmd[1])] = False
    elif cmd[0] == 'check':
        if arr[int(cmd[1])]:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        arr[int(cmd[1])] = not arr[int(cmd[1])]
    elif cmd[0] == 'all':
        arr = [True]*21
    elif cmd[0] == 'empty':
        arr = [False]*21