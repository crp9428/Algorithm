import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
for i in range(T):
    a, b = map(int, input().strip().split())
    print("%d\n" % (a + b))