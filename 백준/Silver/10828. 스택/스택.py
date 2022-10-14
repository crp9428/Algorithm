import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
stack = []
for _ in range(N):
    cmd = list(map(lambda x: int(x) if x.isdigit() else x, input().strip().split()))
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        print("%d\n" % (stack.pop())) if len(stack) > 0 else print("-1\n")
    elif cmd[0] == "size":
        print("%d\n" % len(stack))
    elif cmd[0] == "empty":
        print("0\n") if len(stack) > 0 else print('1\n')
    elif cmd[0] == 'top':
        print("%d\n" % stack[-1]) if len(stack) > 0 else print('-1\n')