import sys
input = sys.stdin.readline
print = sys.stdout.write

while(True):
    try:
        a, b = map(int, input().strip().split())
        print("%d\n" % (a + b))
    except ValueError as e:
        break