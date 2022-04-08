import sys
while True:
    line = sys.stdin.readline()
    if line == '.\n':
        break
    stk = []
    result = True
    for i in list(line):
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] != '(':
                result = False
                break
            else:
                stk.pop()
        elif i == ']':
            if not stk or stk[-1] != '[':
                result = False
                break
            else:
                stk.pop()
    if result and not stk:
        print('yes')
    else:
        print('no')