import sys
input = sys.stdin.readline
print = sys.stdout.write

print("%d\n" % len(set([(int(input().strip()) % 42) for _ in range(10)])))