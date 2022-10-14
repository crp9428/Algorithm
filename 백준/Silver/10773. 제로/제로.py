import sys
input = sys.stdin.readline
print = sys.stdout.write

K, stack = int(input().strip()), list()
for n in list(int(input().strip()) for _ in range(K)):
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print("%d" % sum(stack))