import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
for i in range(1, T + 1):
    a, b = map(int, input().strip().split())
    print("Case #%s: %s\n" % (i, (a + b)))