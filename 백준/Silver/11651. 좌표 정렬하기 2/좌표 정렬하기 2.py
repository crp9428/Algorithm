import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().strip())
arr = sorted(list(tuple(map(int, input().strip().split())) for _ in range(n)), key = lambda x: (x[1], x[0]))
for t in arr:
    print(f"{t[0]} {t[1]}\n")