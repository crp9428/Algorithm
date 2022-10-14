import sys
input = sys.stdin.readline

T = int(input().strip())

for t in range(T):
    ps, stack, isVPS = input().strip(), [], True
    for v in ps:
        if v == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                isVPS = False
            else:
                stack.pop()
    isVPS = isVPS and len(stack) == 0
    print("YES") if isVPS else print("NO")