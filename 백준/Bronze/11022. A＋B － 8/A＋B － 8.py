import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
for i in range(1, T + 1, 1):
    a, b = map(int, input().strip().split())
    print("Case #%d: %d + %d = %d\n" % (i, a, b, a+b))